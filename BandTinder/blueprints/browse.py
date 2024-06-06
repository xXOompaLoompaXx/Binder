from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required

browse_bp = Blueprint("browse", __name__)

@browse_bp.route('/browse')
def browse():
    # Logic to fetch data for discovery goes here
    # You can query your database to fetch bands or artists to display
    
    return render_template('browse.html')


