from flask import Blueprint, render_template, redirect, url_for, flash
from werkzeug.security import generate_password_hash

from app.models.user import User
from app.forms.register_form import RegisterForm
from app.extensions import db


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
        
    return render_template("auth/register.html" ,form=form)

@auth_bp.route("/login",methods=["POST","post"])
def login ():
    return render_template("auth/login.html")