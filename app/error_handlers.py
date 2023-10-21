# error_handling.py
from flask import jsonify

def bad_request_error(e):
    return jsonify({'error': 'Bad Request', 'message': str(e)}), 400

def unauthorized_error(e):
    return jsonify({'error': 'Unauthorized', 'message': str(e)}), 401

def not_found_error(e):
    return jsonify({'error': 'Not Found', 'message': str(e)}), 404

def internal_server_error(e):
    return jsonify({'error': 'Internal Server Error', 'message': str(e)}), 500

def forbidden_error(e):
    return jsonify({'error': 'Forbidden', 'message': str(e)}), 403

def conflict_error(e):
    return jsonify({'error': 'Conflict', 'message': str(e)}), 409

