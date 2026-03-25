from flask import Flask
from config import Config
from models import db

from controllers.auth_controller import auth_bp
from controllers.email_controller import email_bp

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

app.register_blueprint(auth_bp)
app.register_blueprint(email_bp)

if __name__ == "__main__":
    app.run(debug=True)