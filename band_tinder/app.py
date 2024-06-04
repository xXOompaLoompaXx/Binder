from flask import Flask, request, render_template
from blueprints.mainpage.mainpage import mainpage_bp
app = Flask(__name__)

app.register_blueprint(mainpage_bp)

if __name__ == '__main__':
    app.run(debug=True)
    
