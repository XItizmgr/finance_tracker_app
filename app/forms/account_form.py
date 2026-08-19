from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, DecimalField, SubmitField
from wtforms.validators import DataRequired


class AccountForm(FlaskForm):
    account_name = StringField(
        "Enter the Name of ur account", validators=[DataRequired()]
    )

    account_type = SelectField(
        "Select the type",
        choices=[
            ("cash", "Cash"),
            ("bank", "Bank"),
            ("digital_wallet", "Digital Wallet"),
            ("other", "Other"),
        ],
        validators=[DataRequired()],
    )

    balance = DecimalField("Enter the balance", validators=[DataRequired()])

    submit = SubmitField("Add Account")
