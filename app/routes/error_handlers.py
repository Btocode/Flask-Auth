from flask import jsonify, Blueprint

error_routes = Blueprint('error', __name__)


@error_routes.errorhandler(400)
def bad_request(e):
    return jsonify({'error': 'Bad request'}), 400

@error_routes.errorhandler(401)
def unauthorized(e):
    return jsonify({'error': 'Unauthorized'}), 401

@error_routes.errorhandler(404)
def not_found(e):
    return jsonify({'error': 'Not found'}), 404

@error_routes.errorhandler(500)
def internal_server_error(e):
    return jsonify({'error': 'Internal Server Error'}), 500
