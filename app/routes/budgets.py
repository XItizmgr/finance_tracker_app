from flask import Blueprint , redirect , url_for , render_template
from flask_login import login_required

budget_bp = Blueprint("budget",__name__)

@budget_bp.route("/budget")
@login_required
def budget():
    return render_template("budget.html")