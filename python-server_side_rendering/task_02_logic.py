#!/usr/bin/python3
"""
Flask application to render static and dynamic pages.
Reads items from a JSON file and displays them using Jinja templates.
"""

from flask import Flask, json, render_template

app = Flask(__name__)

@app.route('/items')
def items():
    """Read items from JSON and render the items page."""
    with open('items.json') as file:
        items = json.load(file).get('items')
    return render_template('items.html', items=items)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
