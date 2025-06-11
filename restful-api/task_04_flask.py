#!/usr/bin/python3

from flask import Flask, jsonify, request, abort

app = Flask(__name__)

users = {}

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


if __name__ == "__main__": app.run()