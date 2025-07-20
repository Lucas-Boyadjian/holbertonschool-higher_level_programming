#!/usr/bin/python3
"""
Flask application to render static and dynamic product pages.
Reads product data from JSON or CSV files and displays them using Jinja
templates. Supports filtering by product id and error handling
for invalid sources or missing products.
"""

from flask import Flask, json, render_template, request
import csv
import sqlite3

app = Flask(__name__)


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

    elif source == 'sql':
        try:
            con = sqlite3.connect('products.db')
            cur = con.cursor()
            if id:
                cur.execute("SELECT id, name, price, category FROM Products WHERE id=?", (id,))
            else:
                cur.execute("SELECT id, name, price, category FROM Products")
            rows = cur.fetchall()
            products = [
                {"id": row[0], "name": row[1], "price": row[2], "category": row[3]}
                for row in rows
            ]
            con.close()
        except Exception:
            return render_template('product_display.html', error="Database error")
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
    elif id and source == 'sql' and not products:
        return render_template('product_display.html', error="Product not found")

    return render_template('product_display.html', products=products)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
