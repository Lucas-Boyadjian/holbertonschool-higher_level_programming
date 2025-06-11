#!/usr/bin/python3
"""
Simple Flask API for managing users.

This module implements a RESTful API using Flask to perform basic
CRUD operations on a collection of users stored in memory.
"""

from flask import Flask, jsonify, request

app = Flask(__name__)

users = {"jane": {"name": "Jane", "age": 28, "city": "Los Angeles"}}


@app.route('/')
def home():
    """Return welcome message for the API's root endpoint"""
    return 'Welcome to the Flask API!'


@app.route("/data")
def data():
    """Return a list of all usernames in the API"""
    list_names = []
    for user in users.values():
        list_names.append(user["name"])

    return jsonify(list_names)


@app.route("/status")
def status():
    """Return status of the API"""
    return jsonify({"status": "OK"})


@app.route("/users/<username>")
def user_name(username):
    """Return the full user object for the specified username"""
    if username in users:
        return jsonify(users[username])


@app.route("/add_user", methods=["POST"])
def user_add():
    """Add a new user to the users dictionary

    Expects JSON data with username, name, age, and city
    """
    data = request.get_json()
    username = data.get('username')

    new_user = {"name": data.get('name', ''), "age": data.get('age', 0),
                "city": data.get('city', '')}

    users[username] = new_user

    return jsonify({"message": f"User {username} added successfully",
                    "user": new_user})


if __name__ == "__main__":
    app.run()
