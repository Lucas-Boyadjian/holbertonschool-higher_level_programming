#!/usr/bin/python3
"""
Simple HTTP server module implementing a basic REST API.

This module creates a HTTP server that responds to different endpoints
with various JSON responses or plain text. It demonstrates the basics
of creating a RESTful API using Python's built-in http.server module.
"""

import http.server
import json


class Serveur(http.server.BaseHTTPRequestHandler):
    """
    HTTP request handler class that implements a simple REST API.

    This class handles GET requests to different endpoints and returns
    appropriate responses with different content types and status codes.
    """

    def do_GET(self):
        """
        Handle GET requests to different API endpoints.

        Routes:
            - /: Returns a welcome message in plain text
            - /data: Returns sample user data as JSON
            - /status: Returns API status information
            - /info: Returns API version and description
            - Any other path: Returns a 404 error
        """

        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'Hello, this is a simple API!')

        elif self.path == '/data':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            dict_data = json.dumps({"name": "John", "age": 30,
                                   "city": "New York"})
            self.wfile.write(dict_data.encode())

        elif self.path == '/status':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"OK")

        elif self.path == '/info':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            json_info = json.dumps({
                "version": "1.0",
                "description": "A simple API built with http.server"
            })
            self.wfile.write(json_info.encode())

        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"Endpoint not found")


if __name__ == "__main__":
    server_address = ('', 8000)
    httpd = http.server.HTTPServer(server_address, Serveur)
    httpd.serve_forever()
