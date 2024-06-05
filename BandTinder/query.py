import psycopg2
from typing import Any
import os
from BandTinder.models import User
from BandTinder import conn, cur


#Generic Query
def query(sql : str, vars: Any | None = None):
    cur.execute(sql, vars)
    conn.commit()


def insert_user(name, username, password):
    sql = """
        INSERT INTO Users(full_name, user_name, password)
            VALUES (%s, %s, %s)
    """
    query(sql, (name, username, password))


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


def get_cities():
    sql = """
    SELECT * FROM Cities
    """
    cur.execute(sql)


    return cur.fetchall()