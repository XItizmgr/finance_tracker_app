from flask_wtf import FlaskForm
from wtforms import StringField,DecimalField
from wtforms.validators import data_required 


class budgetForm():
    name  = StringField("Enter the name of ur budget",validators=[data_required()])
    ammount = DecimalField("Enter the ammount for ur budget",validators=[data_required()])