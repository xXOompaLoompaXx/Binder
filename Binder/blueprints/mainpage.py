from flask import Blueprint, render_template
from flask_login import login_required, current_user
import Binder.query as query

mainpage_bp = Blueprint("mainpage", __name__)

@mainpage_bp.route('/')
def hello_world():
    return render_template("index.html")


@mainpage_bp.route('/bands', methods=["GET"])
@login_required
def user_bands():
    user_bands = query.get_bands_by_user(current_user.id)
    bands_with_members = []
    for band in user_bands:
        members = query.get_band_players(band['band_id'])
        band['members'] = members
        bands_with_members.append(band)
    return render_template("profiles/my_bands.html", user_bands=bands_with_members)