from flask import Blueprint,render_template

dash_bp = Blueprint("dashboard",__name__)

@dash_bp.route("/dashboard")
def dashboard():
    return render_template("dashboard/dashboard.html")