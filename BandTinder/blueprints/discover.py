# discover.py

from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required, current_user
import BandTinder.query as query

discover_bp = Blueprint("discover", __name__)

@discover_bp.route('/discover')
@login_required
def discover():
    #Pick random band, then display it.
    matched_bands = []
    return render_template('discover.html', matched_bands=matched_bands)

@discover_bp.route('/confirm_interest/<int:band_id>', methods=["POST"])
@login_required
def confirm_interest(band_id):
    query.set_user_interest(current_user.id, band_id, True)
    return redirect(url_for('discover.discover'))

@discover_bp.route('/decline_interest/<int:band_id>', methods=["POST"])
@login_required
def decline_interest(band_id):
    query.set_user_interest(current_user.id, band_id, False)
    return redirect(url_for('discover.discover'))


