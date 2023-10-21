# Using flask to make an api
# import necessary libraries and functions
from flask import Flask, jsonify, request, Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from datetime import timedelta
from flask_migrate import Migrate
from flask_restful import Api
from .error_handlers import *


# creating a Flask app
# Define the database object outside the app instance
db = SQLAlchemy()
api = Api()


def create_app():
    from .routes.app_routes import app_routes

    app = Flask(__name__)

    app.register_error_handler(400, bad_request_error)
    app.register_error_handler(401, unauthorized_error)
    app.register_error_handler(404, not_found_error)
    app.register_error_handler(500, internal_server_error)

    app.config.from_pyfile("config.py")
    app.config["JWT_SECRET_KEY"] = "your-secret-key"
    app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(
        hours=1
    )  # Set the expiration time to 1 hour

    jwt = JWTManager(app)
    migrate = Migrate(app, db)

    # Initialize the database with the Flask app
    db.init_app(app)

    #
    api.init_app(app)
    # Register the Blueprints
    app.register_blueprint(app_routes)

    return app, api
