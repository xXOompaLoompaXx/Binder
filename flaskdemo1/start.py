from flask import Flask, request, render_template

app = Flask(__name__)

import psycopg2
from psycopg2.extras import RealDictCursor



conn = psycopg2.connect(
    host="localhost",
    database="band_tinder",
    user="postgres",
    password="620907hyty"
)



cur = conn.cursor(cursor_factory=RealDictCursor)




@app.route("/insert", methods=['POST'])
def insert_instrument():
    sql = """
    INSERT INTO Instrument(instrumentType)
    VALUES ('Guitar')
    """
    print("hej")
    cur.execute(sql)
    conn.commit()

@app.route('/')
def hello_world():
    return render_template("index.html")