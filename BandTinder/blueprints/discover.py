from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required

discover_bp = Blueprint("discover", __name__)

@discover_bp.route('/discover')
@login_required  # Add this to ensure only logged-in users can access the discover page
def discover():
    # Logic to fetch data for discovery goes here
    # You can query your database to fetch bands or artists to display
    
    return render_template('discover.html')


