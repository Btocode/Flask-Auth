# resources/user_registration_resource.py
from flask_restful import Resource, reqparse
from flask import request, jsonify
from app import db
from app.models.users import User

class UserRegistrationResource(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('username', type=str, required=True, help='Username is required')
        self.parser.add_argument('password', type=str, required=True, help='Password is required')
        self.parser.add_argument('email', type=str, required=True, help='Email is required')
        self.parser.add_argument('full_name', type=str, required=True, help='Full Name is required')

    def post(self):
        args = self.parser.parse_args()
        username = args['username']
        password = args['password']
        email = args['email']
        full_name = args['full_name']

        # Check if the username or email already exists in the database
        if User.query.filter_by(username=username).first() is not None:
            return jsonify({'error': 'Username already exists'}), 400
        if User.query.filter_by(email=email).first() is not None:
            return jsonify({'error': 'Email already in use'}), 400

        # Create a new User instance
        new_user = User(username=username, email=email, full_name=full_name)
        new_user.set_password(password)

        # Add the user to the database
        db.session.add(new_user)
        db.session.commit()

        return jsonify({'message': 'User registered successfully'})
