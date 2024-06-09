from flask import Blueprint, render_template, flash, redirect
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
import BandTinder.query as query
import requests
from apscheduler.schedulers.background import BackgroundScheduler
import randomname

matching_bp = Blueprint("matching", __name__ )


def try_generate_band_for_user(pk):
    genre, user_instrument = query.get_user_genre_instrument(pk)
    instruments = query.get_typical_instrument_for_genre(genre)
    instruments.remove(user_instrument)

    names = ["pk0.pk as pk0"]
    for i in range(len(instruments)):
        names.append(f"pk{i + 1}.pk as pk{i + 1}")

    selectNames = ", ".join(names)
    sql = f"""
    SELECT DISTINCT {selectNames}
    FROM 
    (SELECT pk from users where pk = {pk}) pk0, 
    """
    parts = []
    for i in range(len(instruments)):
        ins = instruments[i]
        parts.append (f"""
        (SELECT PG.pk
        FROM Prefers_Genre PG, Plays P
        WHERE PG.pk=P.pk and PG.genre='{genre}' and P.instrument='{ins}') pk{i + 1}
        """)
    sql += ",".join(parts)
    combinations = query.get_query(sql)

    for row in combinations:
        lst = [value for value in dict(row).values()]
        if not query.get_bands_with_player_ids (lst):
            #generate band with players
            query.make_band((randomname.get_name(adj=('shape','weather','emotions','speed'), noun=('music_instruments')).replace('-',' '))+'s', genre, lst)
            return True
    
    return False



def loner_fix():
    loners =  query.get_lonely_users()
    for pk in loners:
        result = try_generate_band_for_user(pk)
        print(f"found lonely user: {pk}, making band. Made band: {result}")
        
            
loner_fix()
scheduler = BackgroundScheduler()
scheduler.add_job(func=loner_fix, trigger="interval", seconds=10)
scheduler.start()

@matching_bp.route('/matcher')
def matcher():
    pass

# @matching_bp.route('/demo')
# def demo():
# scheduled_task()