import os
import psycopg2
from psycopg2.extras import RealDictCursor
from flask import Flask, g, send_from_directory, request
from flask_login import current_user, LoginManager
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
app.config['SECRET_KEY'] = "verysecretkey"

login_manager = LoginManager(app)
login_manager.init_app(app)

# Database setup
DATABASE_URL = os.getenv('DATABASE_URL')

conn = None
cur = None

try:
    if DATABASE_URL:
        conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    else:
        # Fallback for local development if DATABASE_URL is not set
        from dotenv import load_dotenv, find_dotenv
        load_dotenv(dotenv_path="../.env", override=False)
        
        conn = psycopg2.connect(
            host=os.getenv("DB_HOST"),
            database=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("psqlPass")
        )
    cur = conn.cursor(cursor_factory=RealDictCursor)
except Exception as e:
    print(f"Error connecting to database: {e}")

@app.before_request
def before_request():
    if request.endpoint and 'static' not in request.endpoint:
        g.user = current_user if current_user.is_authenticated else None
        if g.user:
            g.user_name = current_user.user_name
            g.full_name = current_user.full_name
        else:
            g.user_name = None
            g.full_name = None

@app.route('/static/<path:filename>')
def static_files(filename):
    return send_from_directory(app.static_folder, filename)

from Binder.blueprints.mainpage import mainpage_bp
from Binder.blueprints.loginpage import loginpage_bp
from Binder.blueprints.profiles import profiles_bp
from Binder.blueprints.matching import matching_bp
from Binder.blueprints.discover import discover_bp
from Binder.blueprints.browse import browse_bp

app.register_blueprint(browse_bp)
app.register_blueprint(discover_bp)
app.register_blueprint(matching_bp)
app.register_blueprint(profiles_bp)
app.register_blueprint(mainpage_bp)
app.register_blueprint(loginpage_bp)
