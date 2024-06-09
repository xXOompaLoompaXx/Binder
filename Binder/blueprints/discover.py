# discover.py
from Binder.blueprints.matching import loner_fix
from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required, current_user
import Binder.query as query

discover_bp = Blueprint("discover", __name__)

@discover_bp.route('/discover')
@login_required
def discover():
    # Pick randomnly compatible band, then display it.
    pk = current_user.pk
    unanswered_bands = query.get_unanswered_bands(pk)
    if len(unanswered_bands) > 0:
        band = unanswered_bands[0]
        players = query.get_band_players(band["band_id"])
    else:
        band = None
        players = None
    return render_template('discover.html', band=band, players = players)

@discover_bp.route('/confirm_interest/<int:band_id>', methods=["POST"])
@login_required
def confirm_interest(band_id):
    query.set_user_interest(current_user.id, band_id, True)
    query.update_bands_match_status()
    loner_fix()
    return redirect(url_for('discover.discover'))

@discover_bp.route('/decline_interest/<int:band_id>', methods=["POST"])
@login_required
def decline_interest(band_id):
    query.set_user_interest(current_user.id, band_id, False)
    query.set_band_state(band_id, 2)
    loner_fix()
    return redirect(url_for('discover.discover'))


