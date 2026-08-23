from flask import Blueprint,render_template

ver_bp = Blueprint("ver",__name__)

@ver_bp.route("/setting")
def setting():
    return render_template("version2.html")