from flask_wtf import FlaskForm
from wtforms import PasswordField, SubmitField
from wtforms.validators import DataRequired, length, EqualTo


class PasswordRest(FlaskForm):
    Password = PasswordField(
        "New Password", validators=[DataRequired(), length(max=100, min=6)]
    )
    Confirm_password = PasswordField(
        "Confirm password ",
        validators=[DataRequired(), EqualTo("Password", message="Password not match")],
    )
    Submit = SubmitField("Reset Password")