import psycopg2
from psycopg2.extras import RealDictCursor
from typing import Any
import os




conn = psycopg2.connect(
    host="localhost",
    database="band_tinder",
    user="postgres",
    password="620907hyty"
)

cur = conn.cursor(cursor_factory=RealDictCursor)



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


def getUserByUsername(username):
    sql = """
        SELECT * FROM Users where user_name = %s
    """



    cur.execute(sql, (username,))
    result = cur.fetchone()
    return result
    