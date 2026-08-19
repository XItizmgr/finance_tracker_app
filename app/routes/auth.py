from flask import Blueprint, render_template, redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash

from app.models.user import User
from app.forms.register_form import RegisterForm
from app.forms.login_form import loginForm
from app.extensions import db
from flask_login import login_user

from app.forms.Forget_password_form import ForgetPassword
from app.forms.password_reset_form import PasswordRest
from app.utils.helpers import generate_reset_token
from app.utils.helpers import verify_reset_token
from app.services.email_service import send_password_reset_link


auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        existing_user = User.query.filter_by(email=form.email.data).first()
        if existing_user:
            flash("An account with this email already register")
            return render_template("auth/register.html", form=form)
        hashed_password = generate_password_hash(form.password.data)
        new_user = User(
            username=form.username.data,
            email=form.email.data,
            password_hash=hashed_password,
        )
        db.session.add(new_user)
        db.session.commit()
        flash("Account created successfully!")
        return redirect(url_for("auth.login"))

    return render_template("auth/register.html", form=form)


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    form = loginForm()
    if form.validate_on_submit():
        existing_user = User.query.filter_by(email=form.Email.data).first()

        if not existing_user:
            flash("Invalid email", "error")
            return render_template("auth/login.html", form=form)
        if not check_password_hash(existing_user.password_hash, form.password.data):
            flash("Incorrect password.", "error")
            return render_template("auth/login.html", form=form)
        login_user(existing_user, remember=form.remember_me.data)
        flash("Login successful!", "success")
        return redirect(url_for("dashboard.dashboard"))
    return render_template("auth/login.html", form=form)


@auth_bp.route("/base")
def base():
    return render_template("base.html")


@auth_bp.route("/forget_password", methods=["GET", "POST"])
def forgetPassword():
    form = ForgetPassword()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.Email.data).first()

        if user:
            token = generate_reset_token(user.user_id)

            reset_url = url_for("auth.passwordReset", token=token, _external=True)

            send_password_reset_link(user.email, reset_url)
            flash(
                "A password reset link has been sent.",
                "info",
            )
            return redirect(url_for("auth.login"))
        flash(
            "If an account exists with that email, "
            "a password reset link has been sent.",
            "info",
        )

    return render_template("auth/forget_password.html", form=form)

@auth_bp.route("/reset_password/<token>", methods=["POST", "GET"])
def passwordReset(token):
    user_id = verify_reset_token(token)
    if user_id is None:
        flash("The reset link is invalid or has expired.", "danger")
        return redirect(url_for("auth.forgetPassword"))
    user = User.query.get(user_id)
    if user is None:
        flash("Invalid reset link.", "danger")
        return redirect(url_for("auth.forgetPassword"))
    form = PasswordRest()
    if form.validate_on_submit():
        if check_password_hash(user.password_hash, form.Password.data):
            flash(
                "New password must be different from your current password.", "warning"
            )
        else:
            user.password_hash = generate_password_hash(form.Password.data)
            db.session.commit()
            flash("Your password has been reset successfully.", "success")
            return redirect(url_for("auth.login"))
    return render_template("auth/password_reset.html", form=form, token=token)
