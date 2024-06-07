import psycopg2
from typing import Any, List
from BandTinder.models import User
from BandTinder import conn, cur


def query(sql: str, vars: Any = None):
    cur.execute(sql, vars)
    conn.commit()



def get_query(sql: str, vars: Any = None):
    cur.execute(sql, vars)
    return cur.fetchall()


def insert_user(name, username, password, birth_date, located_in, instrument, proficiency, genre):
    sql = """
        INSERT INTO Users (full_name, user_name, password, birth_date, located_in)
        VALUES (%s, %s, %s, %s, %s) RETURNING pk;
    """
    cur.execute(sql, (name, username, password, birth_date, located_in))
    user_id = cur.fetchone()["pk"]
    conn.commit()

    sql = """
        INSERT INTO Plays (pk, instrument, proficiency) VALUES (%s, %s, %s);
        INSERT INTO Prefers_Genre (pk, genre) VALUES (%s, %s);
    """
    cur.execute(sql, (user_id, instrument, proficiency, user_id, genre))
    conn.commit()



def get_user_class_by_user_name(user_name):
    sql = """
    SELECT * FROM Users
    WHERE user_name = %s
    """
    cur.execute(sql, (user_name,))
    user_data = cur.fetchone()
    return User(user_data) if user_data else None


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
    sql = """
    SELECT U.pk
    FROM Users U
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
    cur.execute(sql, (pk,))
    result = cur.fetchone()
    return (result["genre"], result["instrument"]) if result else (None, None)


def get_cities():
    sql = """
    SELECT * FROM Cities
    """
    cur.execute(sql)
    return cur.fetchall()


def make_band(name, genre, user_lst):
    sql = """
    INSERT INTO Bands (band_name, band_genre, band_state, creation_date) VALUES
    (%s, %s, 0, NOW()::DATE) returning band_id
    """
    cur.execute(sql, (name, genre))
    band_id = cur.fetchone()["band_id"]
    conn.commit()

    for pk in user_lst:
        sql = """
        INSERT INTO Band_contains (pk, band_id, interested) VALUES
        (%s, %s, FALSE);
        """
        query(sql, (pk, band_id))



def get_bands_with_player_ids(ids: List[int]):
    sql = """
    SELECT band_id
    FROM band_contains
    WHERE pk IN %s
    GROUP BY band_id
    HAVING COUNT(DISTINCT pk) = %s;
    """
    cur.execute(sql, (tuple(ids), len(ids)))
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


def get_bands_by_user(user_id):
    sql = """
    SELECT B.band_id, B.band_name, B.band_genre, B.creation_date
    FROM Bands B
    JOIN Band_contains BC ON B.band_id = BC.band_id
    WHERE BC.pk = %s AND B.band_state = 1
    """
    cur.execute(sql, (user_id,))
    return cur.fetchall()

def get_users_genre_instrument(genre, instrument):
    sql = """
    SELECT PG.pk
    FROM Prefers_Genre PG, Plays P
    WHERE PG.pk=P.pk and PG.genre=%s and P.instrument=%s
    """
    cur.execute(sql, (genre, instrument))
    return [row["pk"] for row in cur.fetchall()]


def set_user_interest(user_id, band_id, match_status):
    sql = """
    UPDATE Band_contains
    SET interested = %s
    WHERE pk = %s AND band_id = %s
    """
    cur.execute(sql, (match_status, user_id, band_id))
    conn.commit()

def get_matched_bands(user_id):
    sql = """
    SELECT B.band_id
	FROM BANDS B
    WHERE NOT EXISTS (
        SELECT 1 FROM Band_contains BC
        WHERE BC.band_id = B.band_id AND (BC.interested = FALSE OR BC.interested IS NULL)
    )
    """
    cur.execute(sql, (user_id,))
    return cur.fetchall()
