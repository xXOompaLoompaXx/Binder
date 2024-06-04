
from flask import Blueprint, render_template
from BandTinder.query import query
import requests

mainpage_bp = Blueprint("mainpage", __name__)


@mainpage_bp.route('/')
def hello_world():
    return render_template("index.html")