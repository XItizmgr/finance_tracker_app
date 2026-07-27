from flask import Flask
from app.config import Config
from app.extensions import db, login_manager, migrate
from app.routes.auth import auth_bp
from app.routes.main import main_bp
from app.routes.dashboard import dash_bp
def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app, db)
    app.register_blueprint(auth_bp)
    app.register_blueprint(main_bp)
    app.register_blueprint(dash_bp)
    from app.models import User, Account, Category,Budget,Notification,Saving,Transaction
    return app
@login_manager.user_loader
def load_user(user_id):
    from app.models.user import User
    return User.query.get(int(user_id))

