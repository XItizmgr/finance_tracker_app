from app.extensions import db


class Notification(db.Model):
    __tablename__ = "notifications"
    notification_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"), nullable=False)
    title = db.Column(db.String(250), nullable=False)
    message = db.Column(db.String(500), nullable=False)
    notification_type = db.Column(db.String(100))
    priority = db.Column(db.String(50), nullable=False, default="medium")
    action_url = db.Column(db.String(255), nullable=True)
    is_read = db.Column(db.Boolean, nullable=False, default=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    read_at = db.Column(db.DateTime, nullable=True)
