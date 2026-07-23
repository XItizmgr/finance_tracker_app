from app.extensions import db
class Saving(db.Model):
    __tablename__="savings"
    goal_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"), nullable=False)
    account_id = db.Column(db.Integer,db.ForeignKey("accounts.account_id"), nullable=False)
    goal_name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(250), nullable=True)
    target_amount = db.Column(db.Numeric(12, 2),nullable=False)
    current_amount = db.Column(db.Numeric(12, 2),nullable=False)
    deadline = db.Column(db.Date,nullable = False)
    status = db.Column(db.String(50),default = "active",nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime,server_default = db.func.now(),onupdate=db.func.now())