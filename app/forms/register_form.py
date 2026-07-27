from flask_wtf import FlaskForm
from wtforms.validators import data_required, email, length, equal_to
from wtforms import StringField, PasswordField, SubmitField, EmailField


class RegisterForm(FlaskForm):
    username = StringField(
        "Full Name", validators=[data_required(), length(min=6, max=100)]
    )
    email = EmailField("Email Address", validators=[data_required(), email()])
    password = PasswordField(
        "Password", validators=[data_required(), length(min=6, max=100)]
    )
    confirm_password = PasswordField(
        "Confirm Password", validators=[data_required(), equal_to("password")]
    ) 
    submit = SubmitField("Create Account")




