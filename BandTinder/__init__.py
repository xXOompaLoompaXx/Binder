
from flask import Flask, g
from flask_login import current_user, LoginManager
import os
import psycopg2
from psycopg2.extras import RealDictCursor

app = Flask(__name__)
app.config['SECRET_KEY'] = "shrekisverycool"

login_manager = LoginManager(app)
login_manager.init_app(app)

# Database setup
conn = psycopg2.connect(
    host="localhost",
    database="band_tinder",
    user="postgres",
    password=os.getenv("psqlPass")
)
cur = conn.cursor(cursor_factory=RealDictCursor)

@app.before_request
def before_request():
    g.user = current_user if current_user.is_authenticated else None
    g.user_name = current_user.user_name if current_user.is_authenticated else None
    g.full_name = current_user.full_name if current_user.is_authenticated else None

from BandTinder.blueprints.mainpage import mainpage_bp
from BandTinder.blueprints.loginpage import loginpage_bp
from BandTinder.blueprints.profiles import profiles_bp
from BandTinder.blueprints.matching import matching_bp
from BandTinder.blueprints.discover import discover_bp
from BandTinder.blueprints.browse import browse_bp

app.register_blueprint(browse_bp)
app.register_blueprint(discover_bp)
app.register_blueprint(matching_bp)
app.register_blueprint(profiles_bp)
app.register_blueprint(mainpage_bp)
app.register_blueprint(loginpage_bp)
