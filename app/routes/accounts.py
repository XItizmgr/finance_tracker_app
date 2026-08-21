from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required, current_user

from app.forms.account_form import AccountForm
from app.models.account import Account
from app.extensions import db


acc_bp = Blueprint("acc", __name__)


@acc_bp.route("/account", methods=["GET", "POST"])
@login_required
def account():

    form = AccountForm()

    if form.validate_on_submit():
        new_account = Account(
            account_name=form.account_name.data,
            account_type=form.account_type.data,
            balance=form.balance.data,
            user_id=current_user.user_id,
        )

        db.session.add(new_account)
        db.session.commit()

        flash("Your account is successfully created :)", "success")

        return redirect(url_for("acc.account"))

    accounts = Account.query.filter_by(user_id=current_user.user_id).all()

    return render_template("account.html", form=form, accounts=accounts)


@acc_bp.route("/account/edit/<int:account_id>", methods=["POST"])
@login_required
def editAccount(account_id):
    account = Account.query.filter_by(
        account_id=account_id, user_id=current_user.user_id
    ).first_or_404()

    form = AccountForm(obj=account)

    if form.validate_on_submit():
        account.account_name = form.account_name.data
        account.account_type = form.account_type.data
        account.balance = form.balance.data
        db.session.commit()

        flash("Account updated successfully!", "success")

    return redirect(url_for("acc.account"))
