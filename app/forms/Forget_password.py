from flask_wtf import FlaskForm
from wtforms import EmailField , SubmitField
from wtforms.validators import Email ,DataRequired


class ForgetPassword(FlaskForm):
    Email = EmailField("Email address",validators=[
        DataRequired(),
        Email()
    ])
    Submit = SubmitField("Reset")