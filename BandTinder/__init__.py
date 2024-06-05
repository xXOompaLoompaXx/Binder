from flask import Flask, g
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
import psycopg2
from psycopg2.extras import RealDictCursor
import os

app = Flask(__name__)

app.config['SECRET_KEY'] = "asdasdasdos.getenv('asdSECasdasdasdRasdET_KEYasd')"

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


app.register_blueprint(profiles_bp)
app.register_blueprint(mainpage_bp)
app.register_blueprint(loginpage_bp)



