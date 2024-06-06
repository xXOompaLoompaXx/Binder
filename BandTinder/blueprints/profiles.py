from flask import Blueprint, render_template, flash
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
import BandTinder.query as query
import requests

profiles_bp = Blueprint("profiles", __name__)



@profiles_bp.route('/profile/<username>', methods=["GET"])
def user_profile(username):
    linked_user=query.get_user_class_by_user_name(username)
    if linked_user: 
        if current_user.is_authenticated and current_user["user_name"]==username:
            return render_template("profiles/profile.html")
        else:
            return render_template("profiles/profile_other.html", username=username, linked_user=linked_user)
    else:
        return "404 Page not Found"
    