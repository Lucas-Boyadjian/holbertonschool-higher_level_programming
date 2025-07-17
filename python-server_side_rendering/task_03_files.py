#!/usr/bin/python3
"""
Flask application to render static and dynamic pages, including reading
items from a JSON file and displaying them using Jinja templates.
"""

from flask import Flask, json, render_template, request
import csv

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


@app.route('/products')
def products():
    source = request.args.get('source')
    id = request.args.get('id')

    if source == 'json':
        with open('products.json') as file:
            products = json.load(file)

    elif source == 'csv':
        with open('products.csv') as file:
            reader = csv.DictReader(file)
            products = []
            for row in reader:
                products.append(row)

    else:
        return render_template('product_display.html', error="Wrong source")

    if id:
        products_id = []
        for index in products:
            if str(index.get('id')) == str(id):
                products_id.append(index)
        products = products_id
        if not products:
            return render_template('product_display.html',
                                   error="Product not found")
    return render_template('product_display.html', products=products)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
