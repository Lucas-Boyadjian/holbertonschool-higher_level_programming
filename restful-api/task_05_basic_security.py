#!/usr/bin/python3
"""
Flask API with basic and JWT authentication.

This module implements several authentication methods:
- Basic authentication (username/password)
- JWT token authentication
- Role-based access control
"""

from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import JWTManager
from flask_jwt_extended import jwt_required
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash


app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "super-secret"
jwt = JWTManager(app)
auth = HTTPBasicAuth()

users = {
    "user1": {"username": "user1",
              "password": generate_password_hash("password"), "role": "user"},
    "admin1": {"username": "admin1",
               "password": generate_password_hash("password"), "role": "admin"}
}

tokens = {
    "secret-token-1": "john", "secret-token-2": "susan"
}


@auth.verify_password
def verify_password(username, password):
    """Verifies that the username exists and password is correct"""
    if username in users and check_password_hash(users[username]['password'],
                                                 password):
        return username


@app.route('/basic-protected', methods=["GET"])
@auth.login_required
def verify_user():
    """Route protected by HTTP Basic Authentication"""
    current_user = auth.current_user()
    if current_user not in users:
        return jsonify({"error": "Unauthorized"}), 401
    else:
        return "Basic Auth: Access Granted"


@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    """Handler for requests without a JWT token"""
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    """Handler for malformed JWT tokens"""
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(header, payload):
    """Handler for expired JWT tokens"""
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(header, payload):
    """Handler for revoked JWT tokens"""
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    """Handler for cases where a fresh JWT token is required"""
    return jsonify({"error": "Fresh token required"}), 401


@app.route("/login", methods=["POST"])
def login():
    """Authenticates the user and generates a JWT token"""
    data = request.get_json()
    if not data:
        return jsonify({"error": "Missing JSON data"}), 400

    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({"error": "Missing username or password"}), 400

    if username in users and check_password_hash(users[username]['password'],
                                                 password):
        user_role = {"role": users[username]["role"]}
        access_token = create_access_token(identity=username,
                                           additional_claims=user_role)
        return jsonify(access_token=access_token)
    else:
        return jsonify({"error": "Invalid credentials"}), 401


@app.route("/jwt-protected", methods=["GET"])
@jwt_required()
def jwt_protection():
    """Route protected by JWT authentication"""
    return "JWT Auth: Access Granted"


@app.route("/admin-only", methods=["GET"])
@jwt_required()
def access_admin():
    """Route accessible only to users with admin role"""
    current_user = get_jwt_identity()
    if users[current_user]["role"] != "admin":
        return jsonify({"error": "Admin access required"}), 403
    return "Admin Access: Granted"


if __name__ == '__main__':
    app.run()
