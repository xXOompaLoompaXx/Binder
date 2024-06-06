import psycopg2
from typing import Any
import os
from BandTinder.models import User
from BandTinder import conn, cur


#Generic Query
def query(sql : str, vars: Any | None = None):
    cur.execute(sql, vars)
    conn.commit()


def insert_user(name, username, password, birth_date, located_in, instrument, proficiency, genre):
    sql = """
        INSERT INTO Users(full_name, user_name, password, birth_date, located_in)
            VALUES (%s, %s, %s, %s, %s) RETURNING pk;
    """
    cur.execute(sql, (name, username, password, birth_date, located_in))
    conn.commit()
    id = cur.fetchone()["pk"]
    print(id)
    sql = """
        INSERT INTO Plays (pk, instrument, proficiency) VALUES
        (%s, %s, %s);

        INSERT INTO Prefers_Genre (pk, genre) VALUES
        (%s, %s);
    """
    cur.execute(sql, (id, instrument, proficiency, id, genre))
    conn.commit()
    


def get_user_by_user_name(user_name):
    sql = """
    SELECT * FROM Users
    WHERE user_name = %s
    """
    cur.execute(sql, (user_name,))
    user = User(cur.fetchone()) if cur.rowcount > 0 else None
    return user

def get_instruments():
    sql = """
    SELECT * FROM Instruments
    """
    cur.execute(sql)
    return cur.fetchall()

def get_genres():
    sql = """
    SELECT * FROM Genre
    """
    cur.execute(sql)
    return cur.fetchall()


def get_cities():
    sql = """
    SELECT * FROM Cities
    """

    cur.execute(sql)
    return cur.fetchall()


def getBandsWithPlayerIds(ids: list):
    sql = """
    SELECT band_id
    FROM contains

    """