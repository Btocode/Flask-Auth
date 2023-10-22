# resources/user_registration_resource.py
from flask_restful import Resource, reqparse, abort
from flask import request, jsonify
from app import db
from app.models.users import User
from app.schemas.user_schema import UserSchema
from flask_jwt_extended import create_access_token, jwt_required, create_refresh_token, get_jwt_identity



class UserRegistrationResource(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument(
            "username", type=str, required=True, help="Username is required"
        )
        self.parser.add_argument(
            "password", type=str, required=True, help="Password is required"
        )
        self.parser.add_argument(
            "email", type=str, required=True, help="Email is required"
        )
        self.parser.add_argument(
            "full_name", type=str, required=True, help="Full Name is required"
        )

    def post(self):
        args = self.parser.parse_args()
        username = args["username"]
        password = args["password"]
        email = args["email"]
        full_name = args["full_name"]

        # Check if the username or email already exists in the database
        if User.query.filter_by(username=username).first() is not None:
            abort(400, message="Username already exists")
        if User.query.filter_by(email=email).first() is not None:
            abort(400, message="Email already exists")

        # Create a new User instance
        new_user = User(username=username, email=email, full_name=full_name)
        new_user.set_password(password)

        # Add the user to the database
        db.session.add(new_user)
        db.session.commit()

        return jsonify({"message": "User registered successfully"})

class GetUserResource(Resource):
    @jwt_required()
    def get(self, user_id=None):
        if user_id:
            user = User.query.get(user_id)
            if not user:
                abort(404, message="User not found")
            user_schema = UserSchema()
            result = user_schema.dump(user)
            return jsonify(result)
        else:
            users = User.query.all()
            user_schema = UserSchema(many=True)
            result = user_schema.dump(users)
            return jsonify(result)  

class LoginUserResource(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument(
            "username", type=str, required=True, help="Username is required"
        )
        self.parser.add_argument(
            "password", type=str, required=True, help="Password is required"
        )
    
    def post(self):
        args = self.parser.parse_args()
        username = args["username"]
        password = args["password"]

        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            access_token = create_access_token(identity=user.id, fresh=True)
            refresh_token = create_refresh_token(identity=user.id)
            data = UserSchema().dump(user)
            data["access_token"] = access_token
            data["refresh_token"] = refresh_token
            return jsonify(data)
        else:
            abort(401, message="Invalid username or password")
        
class RefreshTokenResource(Resource):
    @jwt_required(refresh=True)
    def post(self):
        identity = get_jwt_identity()
        access_token = create_access_token(identity=identity, fresh=False)
        refresh_token = create_refresh_token(identity=identity)
        data = {"access_token": access_token, "refresh_token": refresh_token}
        return jsonify(data)


class HealthCheck(Resource):
    def get(self):
        return {
            "message": "API health check!",
            "status": "OK",
        }, 200
