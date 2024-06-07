# discover.py

from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required, current_user
import BandTinder.query as query

discover_bp = Blueprint("discover", __name__)

@discover_bp.route('/discover')
@login_required
def discover():
    matched_bands = query.get_uninterested_bands(current_user.id)
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

@discover_bp.route('/pending')
@login_required
def pending_bands():
    pending_bands = query.get_pending_bands(current_user.id)
    return render_template('pending.html', pending_bands=pending_bands)

@discover_bp.route('/match_band/<int:band_id>', methods=["POST"])
@login_required
def match_band(band_id):
    band = query.get_pending_band_info(current_user.id, band_id)
    if band['all_others_interested']:
        query.finalize_band(current_user.id, band_id, True)
    else:
        flash("Not all other users have shown interest yet.")
    return redirect(url_for('discover.pending_bands'))

@discover_bp.route('/unmatch_band/<int:band_id>', methods=["POST"])
@login_required
def unmatch_band(band_id):
    query.finalize_band(current_user.id, band_id, False)
    return redirect(url_for('discover.pending_bands'))
