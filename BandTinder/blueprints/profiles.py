# profiles.py

from flask import Blueprint, render_template
from flask_login import login_required, current_user
import BandTinder.query as query

profiles_bp = Blueprint("profiles", __name__)

@profiles_bp.route('/profile/<username>', methods=["GET"])
@login_required
def user_profile(username):
    linked_user = query.get_user_class_by_user_name(username)
    if linked_user:
        if current_user.is_authenticated and current_user.user_name == username:
            user_bands = query.get_bands_by_user(current_user.id)
            return render_template("profiles/profile.html", current_user=current_user, user_bands=user_bands)
        else:
            return render_template("profiles/profile_other.html", username=username, linked_user=linked_user, current_user=current_user)
    else:
        return "404 Page not Found"


