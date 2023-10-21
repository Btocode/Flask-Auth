# app/routes/app_routes.py
from flask import jsonify, request, Blueprint, abort
from app import db, api
from sqlalchemy import text
from app.models.users import User
from app.resources.user_resources import *

app_routes = Blueprint("app", __name__)

api.add_resource(HealthCheck, "/")
api.add_resource(UserRegistrationResource, "/auth/register")
api.add_resource(GetUserResource, "/users", "/users/<int:user_id>")
api.add_resource(LoginUserResource, "/auth/login")
