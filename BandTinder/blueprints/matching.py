from flask import Blueprint, render_template, flash, redirect
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
import BandTinder.query as query
import requests
from apscheduler.schedulers.background import BackgroundScheduler

matching_bp = Blueprint("matching", __name__ )


def generate_band_for_user(pk):
    genre = 
    

def scheduled_task():
    for pk in query.get_all_users_pk():
        sql = """
            SELECT * 
            FROM Band_contains BC, Bands
            WHERE BC.pk = %s and Bands.band_state = 0 and Bands.band_id = BC.band_id;
        """
        if len(query.get_query(sql, (pk,))) < 1:
            generate_band_for_user(pk)
            
            

scheduled_task()
scheduler = BackgroundScheduler()
scheduler.add_job(func=scheduled_task, trigger="interval", seconds=60)
scheduler.start()

@matching_bp.route('/matcher')
def matcher():
    pass

# @matching_bp.route('/demo')
# def demo():
# scheduled_task()