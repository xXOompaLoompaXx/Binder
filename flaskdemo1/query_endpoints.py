from start import app
import psycopg2
from psycopg2.extras import RealDictCursor
from flask import Flask, request, render_template


conn = psycopg2.connect(
    host="localhost",
    database="band_tinder",
    user="postgres",
    password="620907hyty"
)



cur = conn.cursor(cursor_factory=RealDictCursor)







