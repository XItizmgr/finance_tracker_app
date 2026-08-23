import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY")

    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")

    SQLALCHEMY_ENGINE_OPTIONS = {"connect_args": {"ssl": {}}}

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    RESEND_API_KEY = os.getenv("RESEND_API_KEY")

    UPLOAD_FOLDER = "app/static/uploads/receipts"

    MAX_CONTENT_LENGTH = 5 * 1024 * 1024

    ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "pdf"}
