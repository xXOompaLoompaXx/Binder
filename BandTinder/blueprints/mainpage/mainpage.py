
from flask import Blueprint, render_template, flash
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
import BandTinder.query as query
import requests

mainpage_bp = Blueprint("mainpage", __name__)


@mainpage_bp.route('/')
def hello_world():
    return render_template("index.html")

@mainpage_bp.route('/profile/<username>', methods=["GET"])
def user_profile(username):
    if query.get_user_by_user_name(username):
        if current_user["user_name"]==username:
            return render_template("profile.html")
        else:
            return render_template("profile_other.html")
    