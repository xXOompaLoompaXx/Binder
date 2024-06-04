import psycopg2
from psycopg2.extras import RealDictCursor
from typing import Any
import os




conn = psycopg2.connect(
    host="localhost",
    database="band_tinder",
    user="postgres",
    password=os.getenv("psqlPass")
)

cur = conn.cursor(cursor_factory=RealDictCursor)



#Generic Query
def query(sql : str, vars: Any | None = None):
    cur.execute()
    conn.commit()