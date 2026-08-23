from flask import Blueprint,render_template
from flask_login import login_required

ver_bp = Blueprint("ver",__name__)

@ver_bp.route("/setting")
@login_required
def setting():
    return render_template("version2.html")