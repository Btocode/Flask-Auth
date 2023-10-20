# app/routes/app_routes.py
from flask import jsonify, request, Blueprint, abort
from app import db, api
from sqlalchemy import text
from app.models.users import User
from app.resources.user_resources import UserRegistrationResource

app_routes = Blueprint("app", __name__)

# app_routes.add_resources(UserRegistrationResource)
api.add_resource(UserRegistrationResource, "/auth/register")


@app_routes.route("/", methods=["GET", "POST"])
def home():
    if request.method == "GET":
        data = "Hello, World"
        return jsonify({"data": data})


@app_routes.route("/home/<int:num>", methods=["GET"])
def disp(num):
    return jsonify({"data": num**2})


@app_routes.route("/test_db_connection", methods=["GET"])
def test_db_connection():
    try:
        # Try performing a simple database query to check the connection
        db.session.execute(text("SELECT 1"))
        return jsonify({"message": "Database connected successfully"})
    except Exception as e:
        return jsonify({"error": "Database connection error", "message": str(e)})

    # @app_routes.route('/auth/register', methods=['POST'])
    # def register():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")
    email = data.get("email")
    full_name = data.get("full_name")

    if not all([username, password, email, full_name]):
        abort(404)

    user = User(username=username, email=email, full_name=full_name)
    user.set_password(password)

    db.session.add(user)
    db.session.commit()

    return jsonify({"message": "User registered successfully"})
