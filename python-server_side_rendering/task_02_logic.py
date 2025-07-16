#!/usr/bin/python3
"""
"""

from flask import Flask, json, render_template

app = Flask(__name__)


@app.route('/')
def home():
    """Render the home page."""
    return render_template('index.html')


@app.route('/about')
def about():
    """Render the about page."""
    return render_template('about.html')


@app.route('/contact')
def contact():
    """Render the contact page."""
    return render_template('contact.html')


@app.route('/items')
def items():
    """Read items from JSON and render the items page."""
    with open('items.json') as file:
        items = json.load(file).get('items')
    return render_template('items.html', items=items)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
