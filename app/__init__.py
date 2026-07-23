from flask import Flask
from app.config import Config
from app.extensions import db, login_manager, migrate
from app.routes.auth import auth_bp
def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app, db)
    app.register_blueprint(auth_bp)
    from app.models import User, Account, Category,Budget,Notification,Saving,Transaction
    return app


