#!/usr/bin/python3
"""
Flask application to render static pages (home, about, contact) 
using Jinja templates. Each route returns its corresponding HTML template.
"""

from flask import Flask, render_template

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


if __name__ == '__main__':
    app.run(debug=True, port=5000)
