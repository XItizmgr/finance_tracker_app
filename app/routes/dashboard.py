from flask import Blueprint, render_template
from flask_login import login_required, current_user
from app.models.account import Account
from app.models.transaction import Transaction
from collections import defaultdict
from datetime import datetime



dash_bp = Blueprint("dashboard", __name__)


@dash_bp.route("/dashboard")
@login_required
def dashboard():


    accounts = Account.query.filter_by(
        user_id=current_user.user_id
    ).all()

    transactions = (
        Transaction.query
        .filter_by(user_id=current_user.user_id)
        .order_by(Transaction.transaction_date.desc())
        .all()
    )

    total_balance = sum(
        float(account.balance)
        for account in accounts
    )

    now = datetime.now()

    current_month = now.strftime("%B")
    current_year = now.year
    current_month_number = now.month

    monthly_transactions = [
        transaction
        for transaction in transactions
        if transaction.transaction_date.month == current_month_number
        and transaction.transaction_date.year == current_year
    ]

    total_income = sum(
        float(transaction.amount)
        for transaction in monthly_transactions
        if transaction.transaction_type == "income"
    )

    total_expense = sum(
        float(transaction.amount)
        for transaction in monthly_transactions
        if transaction.transaction_type == "expense"
    )

    net_balance = total_income - total_expense

    if total_income > 0:
        savings_percentage = (net_balance / total_income) * 100
        savings_percentage = max(
            0,
            min(100, savings_percentage)
        )
    else:
        savings_percentage = 0

    def month_key(year, month):
        return year * 12 + month

    def get_year_month(key):
        year = (key - 1) // 12
        month = ((key - 1) % 12) + 1
        return year, month
    current_key = month_key(
        current_year,
        current_month_number
    )

    monthly_income = defaultdict(float)
    monthly_expense = defaultdict(float)

    for transaction in transactions:

        year = transaction.transaction_date.year
        month = transaction.transaction_date.month

        key = month_key(year, month)

        if transaction.transaction_type == "income":
            monthly_income[key] += float(transaction.amount)

        elif transaction.transaction_type == "expense":
            monthly_expense[key] += float(transaction.amount)

    chart_labels_12 = []
    chart_income_12 = []
    chart_expense_12 = []

    for offset in range(11, -1, -1):

        key = current_key - offset

        year, month = get_year_month(key)

        chart_labels_12.append(
            datetime(year, month, 1).strftime("%b")
        )

        chart_income_12.append(
            round(monthly_income[key], 2)
        )

        chart_expense_12.append(
            round(monthly_expense[key], 2)
        )

    chart_labels_6 = []
    chart_income_6 = []
    chart_expense_6 = []

    for offset in range(5, -1, -1):

        key = current_key - offset

        year, month = get_year_month(key)

        chart_labels_6.append(
            datetime(year, month, 1).strftime("%b")
        )

        chart_income_6.append(
            round(monthly_income[key], 2)
        )

        chart_expense_6.append(
            round(monthly_expense[key], 2)
        )

    all_month_keys = set(
        list(monthly_income.keys())
        + list(monthly_expense.keys())
    )

    all_month_keys = sorted(all_month_keys)

    chart_labels_all = []
    chart_income_all = []
    chart_expense_all = []

    for key in all_month_keys:
        year, month = get_year_month(key)
        chart_labels_all.append(
            datetime(year, month, 1).strftime("%b %Y")
        )

        chart_income_all.append(
            round(monthly_income[key], 2)
        )

        chart_expense_all.append(
            round(monthly_expense[key], 2)
        )
    expense_categories = defaultdict(float)

    for transaction in monthly_transactions:

        if transaction.transaction_type != "expense":
            continue

        if transaction.category:
            category_name = transaction.category.name
        else:
            category_name = "Uncategorized"

        expense_categories[category_name] += float(
            transaction.amount
        )

    expense_labels = list(
        expense_categories.keys()
    )

    expense_values = [
        round(value, 2)
        for value in expense_categories.values()
    ]
    recent_transaction = transactions[:5]

    return render_template(
        "dashboard/dashboard.html",
        accounts=accounts,
        recent_transaction=recent_transaction,
        total_balance=total_balance,
        total_income=total_income,
        total_expense=total_expense,
        net_balance=net_balance,
        savings_percentage=savings_percentage,
        current_month=current_month,
        chart_labels_12=chart_labels_12,
        chart_income_12=chart_income_12,
        chart_expense_12=chart_expense_12,
        chart_labels_6=chart_labels_6,
        chart_income_6=chart_income_6,
        chart_expense_6=chart_expense_6,
        chart_labels_all=chart_labels_all,
        chart_income_all=chart_income_all,
        chart_expense_all=chart_expense_all,
        expense_labels=expense_labels,
        expense_values=expense_values,
    )