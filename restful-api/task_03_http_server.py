#!/usr/bin/python3
"""
Simple HTTP server module implementing a basic REST API.

This module creates a HTTP server that responds to different endpoints
with various JSON responses or plain text. It demonstrates the basics
of creating a RESTful API using Python's built-in http.server module.
"""

import http.server
from http.server import HTTPServer
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
            self.send_header('Content-Type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'Hello, this is a simple API!')

        elif self.path == '/data':
            dict_data = {"name": "John", "age": 30, "city": "New York"}
            data = json.dumps(dict_data)
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(data.encode())

        elif self.path == '/status':
            self.send_response(200)
            self.send_header('Content-Type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'OK')

        elif self.path == '/info':
            info_data = {"version": "1.0", "description":
                         "A simple API built with http.server"}
            info_response = json.dumps(info_data)
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(info_response.encode())

        else:
            self.send_response(404)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            error_mesg = json.dumps({"error": "Endpoint not found"})
            self.wfile.write(error_mesg.encode())


if __name__ == "__main__":
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, Serveur)
    httpd.serve_forever()
