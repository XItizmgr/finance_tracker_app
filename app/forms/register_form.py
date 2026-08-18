from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField, StringField, SubmitField
from wtforms.validators import data_required, email, equal_to, length


class RegisterForm(FlaskForm):
    username = StringField(
        "Full Name", validators=[data_required(), length(min=2, max=100)]
    )
    email = EmailField("Email Address", validators=[data_required(), email()])
    password = PasswordField(
        "Password", validators=[data_required(), length(min=6, max=100)]
    )
    confirm_password = PasswordField(
        "Confirm Password", validators=[data_required(), equal_to("password")]
    ) 
    submit = SubmitField("Create Account")




