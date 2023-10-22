# Using flask to make an api
# import necessary libraries and functions
from flask import Flask, jsonify, request, Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from datetime import timedelta
from flask_migrate import Migrate
from flask_restful import Api
from .error_handlers import *
import os
from dotenv import load_dotenv


# creating a Flask app
# Define the database object outside the app instance
db = SQLAlchemy()
api = Api()


def create_app():
    from .routes.app_routes import app_routes

    app = Flask(__name__)
    load_dotenv()

    app.register_error_handler(400, bad_request_error)
    app.register_error_handler(401, unauthorized_error)
    app.register_error_handler(404, not_found_error)
    app.register_error_handler(500, internal_server_error)

    app.config.from_pyfile("config.py")
    app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET")
    app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(
        hours=1
    )  # Set the expiration time to 1 hour
    app.config["JWT_REFRESH_TOKEN_EXPIRES"] = timedelta(days=30)
    app.config[
        "JWT_ACCESS_DENIED_MESSAGE"
    ] = "You are not authorized to access this resource."
    app.config["JWT_EXPIRED_TOKEN_MESSAGE"] = "Your token has expired."
    app.config["JWT_INVALID_TOKEN_MESSAGE"] = "Invalid token. Please log in again."
    app.config["JWT_REVOKED_TOKEN_MESSAGE"] = "Your token has been revoked."

    jwt = JWTManager(app)
    migrate = Migrate(app, db)

    # Initialize the database with the Flask app
    db.init_app(app)

    api.init_app(app)

    # Register the Blueprints
    app.register_blueprint(app_routes)

    return app
