from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, DecimalField, DateField, SubmitField,TextAreaField
from wtforms.validators import DataRequired


class TransactionForm(FlaskForm):
    title = StringField("Title plzz", validators=[DataRequired()])
    transaction_type = SelectField(
        "Select the type",
        choices=[("expense", "Expense"), ("income", "Income")],
        validators=[DataRequired()],
    )
    amount = DecimalField("Enter the amount", validators=[DataRequired()])
    account_id = SelectField("",validators=[DataRequired()])
    category_id = SelectField("",validators=[DataRequired()])
    description = TextAreaField("Some description about it")
    transaction_date = DateField("Enter your date", validators=[DataRequired()])
    submit = SubmitField("Add Transcation ")
