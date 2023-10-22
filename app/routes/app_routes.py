# app/routes/app_routes.py
from flask import jsonify, request, Blueprint, abort, send_file, url_for
from app import db, api
from sqlalchemy import text
from app.models.users import User
from app.resources.user_resources import *
from app.resources.item_resources import *
from werkzeug.datastructures import FileStorage
from werkzeug.utils import secure_filename
import os
from flask_jwt_extended import (
    create_access_token,
    jwt_required,
    create_refresh_token,
    get_jwt_identity,
)

app_routes = Blueprint("app", __name__)

api.add_resource(HealthCheck, "/")
api.add_resource(UserRegistrationResource, "/auth/register")
api.add_resource(GetUserResource, "/users", "/users/<int:user_id>")
api.add_resource(LoginUserResource, "/auth/login")
api.add_resource(RefreshTokenResource, "/auth/refresh")
api.add_resource(ItemResource, "/items", "/items/<int:item_id>")


def allowed_file(filename):
    print(filename)
    return "." in filename and filename.rsplit(".", 1)[1].lower() in [
        "png",
        "jpg",
        "jpeg",
        "gif",
    ]


def check_size(content_length):
    # check file size is greater than 512kb
    if content_length > 512 * 1024:
        return True
    return False


@app_routes.route("/upload", methods=["POST"])
def upload_file():
    file = request.files["picture"]
    filename = secure_filename(file.filename)

    if not allowed_file(filename):
        return jsonify({"error": "File type not allowed"})
    file_path = os.path.join("app/static/uploads/", filename)

    if check_size(request.content_length):
        print("File size too large")
        return jsonify({"error": "File size too large"})

    file.save(file_path)
    file_url = url_for("app.view_uploaded_file", filename=filename, _external=True)

    return jsonify({"message": "File uploaded successfully", "url": file_url})


# Add a new route to view uploaded files
@app_routes.route("/upload/<filename>", methods=["GET"])
def view_uploaded_file(filename):
    file_path = os.path.join("app/static/uploads/", filename)
    print(file_path)
    # Check if the file exists, and if it does, send it to the client
    if os.path.exists(file_path):
        return send_file(file_path, as_attachment=True)
    else:
        return jsonify({"error": "File not found"}), 404


