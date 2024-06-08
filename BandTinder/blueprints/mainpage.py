from flask import Blueprint, render_template
from flask_login import login_required, current_user
import BandTinder.query as query

mainpage_bp = Blueprint("mainpage", __name__)

@mainpage_bp.route('/')
def hello_world():
    return render_template("index.html")


@mainpage_bp.route('/bands', methods=["GET"])
@login_required
def user_bands():
    user_bands = query.get_bands_by_user(current_user.id)
    return render_template("profiles/user_bands.html", user_bands=user_bands)