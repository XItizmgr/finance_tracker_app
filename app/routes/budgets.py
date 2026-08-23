from flask import Blueprint, redirect, url_for, render_template, flash
from flask_login import login_required, current_user

from app.models.budget import Budget
from app.models.category import Category
from app.models.transaction import Transaction
from app.forms.budget_form import budgetForm
from app.extensions import db


budget_bp = Blueprint("budget", __name__)


@budget_bp.route("/budget", methods=["GET", "POST"])
@login_required
def budget():
    form = budgetForm()
    categories = Category.query.filter_by(user_id=current_user.user_id).all()
    form.category_id.choices = [
        (category.category_id, category.name) for category in categories
    ]
    if form.validate_on_submit():
        new_budget = Budget(
            user_id=current_user.user_id,
            category_id=form.category_id.data,
            name=form.name.data,
            amount=form.amount.data,
            start_date=form.start_date.data,
            end_date=form.end_date.data,
            alert_percentage=form.alert_percentage.data,
        )
        db.session.add(new_budget)
        db.session.commit()
        flash("Budget created successfully!", "success")
        return redirect(url_for("budget.budget"))

    budgets = Budget.query.filter_by(user_id=current_user.user_id).all()
    total_budget = 0
    total_spent = 0

    for budget_item in budgets:
        transactions = Transaction.query.filter(
            Transaction.user_id == current_user.user_id,
            Transaction.category_id == budget_item.category_id,
            Transaction.transaction_type == "expense",
            Transaction.transaction_date >= budget_item.start_date,
            Transaction.transaction_date <= budget_item.end_date,
        ).all()
        spent = sum(float(transaction.amount) for transaction in transactions)
        budget_amount = float(budget_item.amount)
        remaining = budget_amount - spent
        if budget_amount > 0:
            progress = (spent / budget_amount) * 100
        else:
            progress = 0
        progress = min(progress, 100)
        budget_item.spent = spent
        budget_item.remaining = remaining
        budget_item.progress = progress
        total_budget += budget_amount
        total_spent += spent
    total_remaining = total_budget - total_spent
    return render_template(
        "budget.html",
        form=form,
        budgets=budgets,
        categories=categories,
        total_budget=total_budget,
        total_spent=total_spent,
        total_remaining=total_remaining,
    )
