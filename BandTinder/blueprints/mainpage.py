
from flask import Blueprint, render_template, flash
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
import BandTinder.query as query
import requests

mainpage_bp = Blueprint("mainpage", __name__)


@mainpage_bp.route('/')
def hello_world():
    return render_template("index.html")

