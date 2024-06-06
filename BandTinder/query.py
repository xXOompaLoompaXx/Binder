import psycopg2
from typing import Any
import os
from BandTinder.models import User
from BandTinder import conn, cur


#Generic Query
def query(sql : str, vars: Any | None = None):
    cur.execute(sql, vars)
    conn.commit()
    return cur.fetchall()

def get_query(sql : str, vars: Any | None = None):
    cur.execute(sql, vars)
    return cur.fetchall()


def insert_user(name, username, password, birth_date, located_in, instrument, proficiency, genre):
    sql = """
        INSERT INTO Users(full_name, user_name, password, birth_date, located_in)
            VALUES (%s, %s, %s, %s, %s) RETURNING pk;
    """
    cur.execute(sql, (name, username, password, birth_date, located_in))
    conn.commit()
    id = cur.fetchone()["pk"]
    sql = """
        INSERT INTO Plays (pk, instrument, proficiency) VALUES
        (%s, %s, %s);

        INSERT INTO Prefers_Genre (pk, genre) VALUES
        (%s, %s);
    """
    cur.execute(sql, (id, instrument, proficiency, id, genre))
    conn.commit()
    


def get_user_class_by_user_name(user_name):
    sql = """
    SELECT * FROM Users
    WHERE user_name = %s
    """
    cur.execute(sql, (user_name,))
    user = User(cur.fetchone()) if cur.rowcount > 0 else None
    return user

def get_user(pk):
    sql = """
    SELECT * FROM Users WHERE pk = %s
    """
    cur.execute(sql, (pk,))
    return cur.fetchall()

def get_instruments():
    sql = """
    SELECT instrument FROM Instruments
    """
    cur.execute(sql)
    return [row["instrument"] for row in cur.fetchall()]

def get_genres():
    sql = """
    SELECT genre FROM Genre
    """
    cur.execute(sql)
    return [row["genre"] for row in cur.fetchall()]

def get_all_users_pk():
    sql = """
    SELECT pk FROM Users
    """
    cur.execute(sql)
    return [row["pk"] for row in cur.fetchall()]

def get_lonely_users():
    sql ="""
    Select U.pk
    From Users U
    WHERE NOT EXISTS (
        SELECT * 
        FROM Band_contains BC, Bands
        WHERE BC.pk = U.pk and Bands.band_state = 0 and Bands.band_id = BC.band_id
    )
    """
    cur.execute(sql)
    return [row["pk"] for row in cur.fetchall()]


def get_user_genre_instrument(pk):
    sql = """
    SELECT genre, instrument FROM Prefers_genre PG, Plays P where PG.pk = P.pk and PG.pk = %s
    """
    cur.execute(sql, (pk, ))
    result = cur.fetchone()
    return (result["genre"], result["instrument"])


def get_cities():
    sql = """
    SELECT * FROM Cities
    """

    cur.execute(sql)
    return cur.fetchall()


def get_bands_with_player_ids(ids: list):
    sql = """
    SELECT band_id
    FROM band_contains
    WHERE pk IN %s
    GROUP BY band_id
    HAVING COUNT(DISTINCT pk) = %s;
    """
    cur.execute(sql, (tuple(ids),len(ids)))
    return [row["band_id"] for row in cur.fetchall()]

def get_typical_instrument_for_genre(genre):
    sql = """
    SELECT instrument
    FROM Typical_instruments
    WHERE genre = %s
    """
    cur.execute(sql, (genre,))
    return [row["instrument"] for row in cur.fetchall()]

def get_users_with_prefered_genre(genre):
    sql = """
    SELECT pk
    FROM Prefers_Genre
    WHERE genre = %s
    """
    cur.execute(sql, (genre,))
    return [row["pk"] for row in cur.fetchall()]

def get_users_genre_instrument(genre,instrument):
    sql = """
    SELECT PG.pk
    FROM Prefers_Genre PG, Plays P
    WHERE PG.pk=P.pk and PG.genre=%s and P.instrument=%s
    """
    cur.execute(sql, (genre,instrument))
    return [row["pk"] for row in cur.fetchall()]