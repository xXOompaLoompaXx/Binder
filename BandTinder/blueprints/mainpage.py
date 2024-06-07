from flask import Blueprint, render_template
from flask_login import login_required, current_user

mainpage_bp = Blueprint("mainpage", __name__)

@mainpage_bp.route('/')
def hello_world():
    return render_template("index.html")