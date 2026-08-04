from flask import Blueprint, render_template, redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash

from app.models.user import User
from app.forms.register_form import RegisterForm
from app.forms.login_form import loginForm
from app.extensions import db
from flask_login import login_user

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
        return redirect(
            url_for("auth.login")
)

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
        login_user(existing_user,remember = form.remember_me.data)
        flash("Login successful!", "success")
        return redirect(url_for("dashboard.dashboard"))
    return render_template("auth/login.html", form=form)

@auth_bp.route("/base")
def base():
    return render_template("base.html")
