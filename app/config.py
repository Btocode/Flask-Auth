import os
from dotenv import load_dotenv

load_dotenv()

DEBUG = os.getenv("DEBUG", False)
SECRET_KEY = os.getenv("SECRET_KEY", "")
SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI", "")
SQLALCHEMY_TRACK_MODIFICATIONS = False
UPLOAD_FOLDER = '/app/static/images'
