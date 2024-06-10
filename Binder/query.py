# Binder/query.py
from typing import Any, List
from Binder.models import User
from Binder.helpers import execute_query, fetch_all, fetch_one

def insert_user(name, username, password, birth_date, located_in, instrument, proficiency, genre):
    sql = """
        INSERT INTO Users (full_name, user_name, password, birth_date, located_in)
        VALUES (%s, %s, %s, %s, %s) RETURNING pk;
    """
    user_id = fetch_one(sql, (name, username, password, birth_date, located_in))["pk"]

    sql = """
        INSERT INTO Plays (pk, instrument, proficiency) VALUES (%s, %s, %s);
        INSERT INTO Prefers_Genre (pk, genre) VALUES (%s, %s);
    """
    execute_query(sql, (user_id, instrument, proficiency, user_id, genre))

def get_user_class_by_user_name(user_name):
    sql = """
    SELECT * FROM Users
    WHERE user_name = %s
    """
    user_data = fetch_one(sql, (user_name,))
    return User(user_data) if user_data else None

def get_user(pk):
    sql = """
    SELECT * FROM Users WHERE pk = %s
    """
    return fetch_all(sql, (pk,))

def get_instruments():
    sql = """
    SELECT instrument FROM Instruments
    """
    return [row["instrument"] for row in fetch_all(sql)]

def get_genres():
    sql = """
    SELECT genre FROM Genre
    """
    return [row["genre"] for row in fetch_all(sql)]

def get_all_users_pk():
    sql = """
    SELECT pk FROM Users
    """
    return [row["pk"] for row in fetch_all(sql)]

def get_lonely_users():
    sql = """
    SELECT U.pk
    FROM Users U
    WHERE NOT EXISTS (
        SELECT * 
        FROM Band_contains BC, Bands
        WHERE BC.pk = U.pk and Bands.band_state = 0 and Bands.band_id = BC.band_id
    )
    """
    return [row["pk"] for row in fetch_all(sql)]

def get_user_genre_instrument(pk):
    sql = """
    SELECT genre, instrument FROM Prefers_genre PG, Plays P where PG.pk = P.pk and PG.pk = %s
    """
    result = fetch_one(sql, (pk,))
    return (result["genre"], result["instrument"]) if result else (None, None)

def get_cities():
    sql = """
    SELECT * FROM Cities
    """
    return fetch_all(sql)

def make_band(name, genre, user_lst):
    sql = """
    INSERT INTO Bands (band_name, band_genre, band_state, creation_date) VALUES
    (%s, %s, 0, NOW()::DATE) returning band_id
    """
    band_id = fetch_one(sql, (name, genre))["band_id"]

    for pk in user_lst:
        sql = """
        INSERT INTO Band_contains (pk, band_id, interested) VALUES
        (%s, %s, NULL);
        """
        execute_query(sql, (pk, band_id))

def get_bands_with_player_ids(ids: List[int]):
    sql = """
    SELECT band_id
    FROM band_contains
    WHERE pk IN %s
    GROUP BY band_id
    HAVING COUNT(DISTINCT pk) = %s;
    """
    return [row["band_id"] for row in fetch_all(sql, (tuple(ids), len(ids)))]

def get_typical_instrument_for_genre(genre):
    sql = """
    SELECT instrument
    FROM Typical_instruments
    WHERE genre = %s
    """
    return [row["instrument"] for row in fetch_all(sql, (genre,))]

def get_users_with_prefered_genre(genre):
    sql = """
    SELECT pk
    FROM Prefers_Genre
    WHERE genre = %s
    """
    return [row["pk"] for row in fetch_all(sql, (genre,))]

def get_bands_by_user(user_id):
    sql = """
    SELECT B.band_id, B.band_name, B.band_genre, B.creation_date
    FROM Bands B NATURAL JOIN Band_contains BC
    WHERE BC.pk = %s AND B.band_state = 1
    """
    return fetch_all(sql, (user_id,))

def get_users_genre_instrument(genre, instrument):
    sql = """
    SELECT PG.pk
    FROM Prefers_Genre PG, Plays P
    WHERE PG.pk=P.pk and PG.genre=%s and P.instrument=%s
    """
    return [row["pk"] for row in fetch_all(sql, (genre, instrument))]

def set_user_interest(user_id, band_id, match_status):
    sql = """
    UPDATE Band_contains
    SET interested = %s
    WHERE pk = %s AND band_id = %s
    """
    execute_query(sql, (match_status, user_id, band_id))

def set_band_state(band_id, band_state):
    sql = """
    UPDATE Bands
    SET band_state = %s
    WHERE band_id = %s
    """
    execute_query(sql, (band_state, band_id))

def bands_that_have_all_users_interested(): #Finds all the bands that are matched and needs to be set to 1
    sql = """
    SELECT B.band_id
    FROM BANDS B
    WHERE NOT EXISTS (
        SELECT * FROM Band_contains BC
        WHERE BC.band_id = B.band_id AND (BC.interested = FALSE OR BC.interested IS NULL)
    )
    """
    return [row["band_id"] for row in fetch_all(sql)]

def update_bands_match_status():
    bands = bands_that_have_all_users_interested()
    for band_id in bands:
        set_band_state(band_id, 1)

def get_unanswered_bands(user_id):
    sql = """
    SELECT BC.band_id, B.band_name, B.band_genre, B.creation_date
    FROM users u NATURAL JOIN Band_contains BC NATURAL JOIN bands B
    WHERE u.pk=%s and BC.interested IS NULL
    """
    return fetch_all(sql, (user_id,))

def get_band_players(band_id):
    sql = """
    SELECT u.user_name, u.full_name, u.pk, p.instrument
    FROM band_contains bc 
    JOIN Users u on u.pk = bc.pk 
    JOIN plays p on p.pk = u.pk
    WHERE bc.band_id = %s
    """
    return fetch_all(sql, (band_id,))