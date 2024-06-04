from flask import Flask, request, render_template
from blueprints.mainpage.mainpage import mainpage_bp
from blueprints.loginpage.loginpage import loginpage_bp
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from flask_bcrypt import Bcrypt
app = Flask(__name__)

app.register_blueprint(mainpage_bp)
app.register_blueprint(loginpage_bp)


login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

bcrypt = Bcrypt(app)

app.config['SECRET_KEY'] = "asdasdasdos.getenv('asdSECasdasdasdRasdET_KEYasd')"
app.config["bcrypt"] = bcrypt

if __name__ == '__main__':
    app.run(debug=True)
    
