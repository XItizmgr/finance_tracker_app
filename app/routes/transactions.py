from flask import Blueprint, flash, redirect, render_template, url_for, request
from flask_login import login_required, current_user

from app.extensions import db
from app.forms.transaction_form import TransactionForm
from app.models.transaction import Transaction
from app.models.account import Account
from app.models.category import Category

trans_bp = Blueprint("trans", __name__)


@trans_bp.route("/transaction", methods=["POST", "GET"])
@login_required
def transaction():
    form = TransactionForm()
    accounts = Account.query.filter_by(user_id=current_user.user_id).all()
    categories = Category.query.filter_by(user_id=current_user.user_id).all()
    form.account_id.choices = [
        (account.account_id, account.account_name) for account in accounts
    ]
    form.category_id.choices = [
        (category.category_id, category.name) for category in categories
    ]
    if form.validate_on_submit():
        new_transaction = Transaction(
            user_id=current_user.user_id,
            account_id=form.account_id.data,
            category_id=form.category_id.data,
            amount=form.amount.data,
            title=form.title.data,
            description=form.description.data,
            transaction_date=form.transaction_date.data,
            transaction_type=form.transaction_type.data,
        )
        db.session.add(new_transaction)
        db.session.commit()
        flash("Transaction added successfully!", "success")
        return redirect(url_for("trans.transaction"))
    search = request.args.get("search", "").strip()
    transaction_query = Transaction.query.filter_by(user_id=current_user.user_id)
    if search:
        transaction_query = transaction_query.filter(
            Transaction.title.ilike(f"%{search}%")
        )
    transactions = transaction_query.order_by(Transaction.transaction_date.desc()).all()
    return render_template(
        "transaction.html",
        form=form,
        transactions=transactions,
        accounts=accounts,
        categories=categories,
        search=search,
    )


@trans_bp.route("/transaction/edit/<int:transaction_id>", methods=["GET", "POST"])
@login_required
def edit_transaction(transaction_id):
    transaction = Transaction.query.filter_by(
        transaction_id=transaction_id, user_id=current_user.user_id
    ).first_or_404()
    form = TransactionForm()
    accounts = Account.query.filter_by(user_id=current_user.user_id).all()
    categories = Category.query.filter_by(user_id=current_user.user_id).all()
    form.account_id.choices = [
        (account.account_id, account.account_name) for account in accounts
    ]
    form.category_id.choices = [
        (category.category_id, category.name) for category in categories
    ]
    if form.validate_on_submit():
        transaction.title = form.title.data
        transaction.amount = form.amount.data
        transaction.transaction_type = form.transaction_type.data
        transaction.account_id = form.account_id.data
        transaction.category_id = form.category_id.data
        transaction.description = form.description.data
        transaction.transaction_date = form.transaction_date.data
        db.session.commit()
        flash("Transaction updated successfully!", "success")
        return redirect(url_for("trans.transaction"))
    if request.method == "GET":
        form.title.data = transaction.title
        form.amount.data = transaction.amount
        form.transaction_type.data = transaction.transaction_type
        form.account_id.data = transaction.account_id
        form.category_id.data = transaction.category_id
        form.description.data - transaction.description
        form.transaction_date.data = transaction.transaction_date
    return render_template(
        "transaction_edit.html",
        form=form,
        transaction=transaction,
    )
@trans_bp.route("/transaction/delete/<int:transaction_id>", methods=["POST"])
@login_required
def delete_transaction(transaction_id):
    transaction = Transaction.query.filter_by(
        transaction_id=transaction_id, user_id=current_user.user_id
    ).first_or_404()
    db.session.delete(transaction)
    db.session.commit()
    flash("Transaction deleted successfully", "success")
    return redirect(url_for("trans.transaction"))
