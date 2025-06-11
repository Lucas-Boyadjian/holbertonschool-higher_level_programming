#!/usr/bin/python3

from flask import Flask
from flask import jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return 'Welcome to the Flask API!'

@app.route('/data')
def data():
    users = {"jane": {"name": "Jane", "age": 28, "city": "Los Angeles"}}
    
    list_names = []
    for user in users.values():
        list_names.append(user["name"])
    
    return jsonify(list_names) 

if __name__ == "__main__": app.run()

