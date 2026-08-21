from flask_wtf import FlaskForm
from wtforms import StringField, SelectField,SubmitField
from wtforms.validators import DataRequired


class CategoryForm(FlaskForm):
    name = StringField("Category name", validators=[DataRequired()])

    category_type = SelectField(
        "Category type",
        choices=[
            ("expense", "Expense"),
            ("income", "Income"),
        ],
        validators=[DataRequired()],
    )

    submit = SubmitField("Add Category")
