from flask import Blueprint,render_template
from flask_login import login_required

dash_bp = Blueprint("dashboard",__name__)

@dash_bp.route("/dashboard")
@login_required
def dashboard():
    return render_template("dashboard/dashboard.html")