from app.extensions import db


class Category(db.Model):
    __tablename__ = "categories"

    category_id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"), nullable=False)

    name = db.Column(db.String(100), nullable=False)

    category_type = db.Column(db.String(20), nullable=False)
    
    description = db.Column(db.String(255))

    created_at = db.Column(db.DateTime, server_default=db.func.now())

    updated_at = db.Column(
        db.DateTime, server_default=db.func.now(), onupdate=db.func.now()
    )
