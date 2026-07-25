from app.extensions import db
from flask_login import UserMixin


class User(UserMixin,db.Model):
    __tablename__ = "users"
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password_hash = db.Column(db.String(300), nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(
    db.DateTime, server_default=db.func.now(), onupdate=db.func.now()
)
    def get_id(self):
        return str(self.user_id)

