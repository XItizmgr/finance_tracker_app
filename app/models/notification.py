from app.extensions import db
class Notification(db.Model):
    __tablename__ = "notifications"
    notification_id = db.Column(db.Integer,primary_key = True)
    user_id = db.Column(db.Integer,db.ForeignKey("users.user_id"),nullable=False)
    