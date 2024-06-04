from flask import Flask, request, render_template
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
import psycopg2
from psycopg2.extras import RealDictCursor

app = Flask(__name__)

app.config['SECRET_KEY'] = "asdasdasdos.getenv('asdSECasdasdasdRasdET_KEYasd')"

login_manager = LoginManager(app)
login_manager.init_app(app)


# Database setup
conn = psycopg2.connect(
    host="localhost",
    database="band_tinder",
    user="postgres",
    password="pass"
)

cur = conn.cursor(cursor_factory=RealDictCursor)


from BandTinder.blueprints.mainpage.mainpage import mainpage_bp
from BandTinder.blueprints.loginpage.loginpage import loginpage_bp

app.register_blueprint(mainpage_bp)
app.register_blueprint(loginpage_bp)

