# Binder/helpers.py
from psycopg2 import sql
from Binder import cur, conn

def execute_query(query: str, vars: tuple = None):
    if cur is None or conn is None:
        print("Database connection is not available.")
        return None

    try:
        cur.execute(query, vars)
        conn.commit()
        return cur
    except Exception as e:
        print(f"Error executing query: {e}")
        return None

def fetch_all(query: str, vars: tuple = None):
    cursor = execute_query(query, vars)
    if cursor:
        return cursor.fetchall()
    return []

def fetch_one(query: str, vars: tuple = None):
    cursor = execute_query(query, vars)
    if cursor:
        return cursor.fetchone()
    return None
