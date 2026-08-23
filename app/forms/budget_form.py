from flask_wtf import FlaskForm
from wtforms import StringField,DecimalField,SelectField,DateField,SubmitField,IntegerField
from wtforms.validators import DataRequired,NumberRange


class budgetForm(FlaskForm):
    name  = StringField("Enter the name of ur budget",validators=[DataRequired()])
    amount = DecimalField("Enter the ammount for ur budget",validators=[DataRequired()] )
    category_id = SelectField("Category",validators=[DataRequired()])
    start_date = DateField("Enter the Start date",validators=[DataRequired()])
    end_date = DateField("Enter the End date",validators=[DataRequired()])
    alert_percentage = IntegerField("Enter when u want to get the alert " ,validators=[NumberRange(min=0,max=100)] ,default=80)
    submit = SubmitField("Create Budget")
    