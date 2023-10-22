from flask_restful import Resource, reqparse, abort
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import jsonify
from app import db
from app.models.items import Item
from app.schemas.item_schema import ItemSchema
from werkzeug.datastructures import FileStorage
from werkzeug.utils import secure_filename


class ItemResource(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument(
            "name", type=str, required=True, help="Name is required"
        )
        self.parser.add_argument("description", type=str)

    @jwt_required()
    def post(self):
        try:
            user_id = get_jwt_identity()  # Get the user ID from the JWT token
            args = self.parser.parse_args()
            name = args["name"]
            description = args["description"]

            new_item = Item(name=name, description=description, user_id=user_id)

            db.session.add(new_item)
            db.session.commit()

            return jsonify({"message": "Item created successfully"})
        except Exception as e:
            return jsonify({"error": f"An error occurred: {str(e)}"})

    def get(self, item_id=None):
        if item_id:
            # Get the item by ID
            try:
                item = Item.query.get_or_404(item_id)
            except:
                abort(404, message="Requested item not found")
            item_schema = ItemSchema()
            result = item_schema.dump(item)
            return jsonify(result)
        items = Item.query.all()
        item_schema = ItemSchema(many=True)
        result = item_schema.dump(items)
        if not result:
            abort(404, message="No Items found")
        return jsonify(result)

    @jwt_required()
    def put(self, item_id):
        user_id = get_jwt_identity()

        args = self.parser.parse_args()
        name = args["name"]
        description = args["description"]

        # Get the existing item by ID
        try:
            existing_item = Item.query.get_or_404(item_id)
        except:
            abort(404, message="Requested item not found")

        if existing_item.user_id != user_id:
            abort(403, message="Following item does not belong to you")

        existing_item.name = name
        existing_item.description = description
        existing_item.user_id = user_id

        db.session.commit()

        return jsonify({"message": "Item updated successfully"})

    @jwt_required()
    def delete(self, item_id):
        user_id = get_jwt_identity()
        # Get the item by ID
        try:
            item = Item.query.get_or_404(item_id)
        except:
            abort(404, message="Requested item not found")

        if item.user_id != user_id:
            abort(403, message="Following item does not belong to you")
        # Delete the item
        db.session.delete(item)
        db.session.commit()

        return jsonify({"message": "Item deleted successfully"})
