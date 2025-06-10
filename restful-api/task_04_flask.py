#!/usr/bin/python3

from flask import Flask
from flask import jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return 'Welcome to the Flask AP!'

@app.route('/data')
def data():
    users = {"jane": {"name": "Jane", "age": 28, "city": "Los Angeles"}}
    return jsonify(users) 

if __name__ == "__main__": app.run()

