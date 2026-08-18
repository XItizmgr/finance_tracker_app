from flask import current_app
from itsdangerous import URLSafeTimedSerializer


def generate_reset_token(user_id):
    serializer = URLSafeTimedSerializer(current_app.config["SECRET_KEY"])
    token = serializer.dumps({"user_id": user_id})
    return token


def verify_reset_token(token, max_age=600):
    serializer = URLSafeTimedSerializer(current_app.config["SECRET_KEY"])
    try:
        data = serializer.loads(token, max_age=max_age)
        return data["user_id"]
    except Exception:
        return None
