from flask_wtf import FlaskForm
from wtforms import PasswordField, EmailField, SubmitField,BooleanField
from wtforms.validators import data_required, length, email


class loginForm(FlaskForm):
    Email = EmailField("Email address", validators=[data_required(), email()])
    password = PasswordField(
        "Password", validators=[data_required(), length(max=100, min=6)]
    )
    remember_me = BooleanField("Remember me")
    login = SubmitField("Login")
