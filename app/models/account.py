from app.extensions import db

class Account(db.Model):
    __tablename__ = "accounts"
    account_id = db.Column(db.Integer, primary_key=True)
    account_name = db.Column(db.String(100), nullable=False)
    account_type = db.Column(db.String(50), nullable=False)
    balance = db.Column(db.Float, default=0)
    user_id = db.Column(db.Integer,db.ForeignKey("users.user_id"),nullable=False
)