
from flask import Blueprint, render_template
from query import query
import requests

mainpage_bp = Blueprint("mainpage", __name__)




@mainpage_bp.route("/insert", methods=['POST'])
def insert_data():
    query("""
        INSERT INTO Instrument(instrumentType)
            VALUES ('Guitar')
    """)
    
@mainpage_bp.route('/')
def hello_world():
    return render_template("index.html")