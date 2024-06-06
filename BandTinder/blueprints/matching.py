from flask import Blueprint, render_template, flash, redirect
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
import BandTinder.query as query
import requests
from apscheduler.schedulers.background import BackgroundScheduler

matching_bp = Blueprint("matching", __name__ )


def generate_band_for_user(pk):
    genre, user_instrument = query.get_user_genre_instrument(pk)
    
    instruments = query.get_typical_instrument_for_genre(genre)
    print(instruments)
    print(user_instrument)
    instruments.remove(user_instrument)

    sql = """
    SELECT DISTINCT *
    FROM 
    (SELECT pk from users where pk = {pk}, 
    """
    parts = []
    for ins in instruments:
        parts.append (f"""
        (SELECT PG.pk
        FROM Prefers_Genre PG, Plays P
        WHERE PG.pk=P.pk and PG.genre='{genre}' and P.instrument='{ins}')
        """)
    sql += ",".join(parts)



def scheduled_task():
    for pk in query.get_lonely_users():
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