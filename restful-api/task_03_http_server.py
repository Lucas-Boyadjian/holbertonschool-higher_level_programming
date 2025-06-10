#!/usr/bin/python3

import http.server
from http.server import HTTPServer
import json

class serveur (http.server.BaseHTTPRequestHandler):

    def do_GET(self):
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
            status_response = json.dumps({'status': 'OK'})
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(status_response.encode())
        
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
            error_mesg = json.dumps({"Endpoint not found"}) 
            self.wfile.write(error_mesg.encode())

server_address = ('', 8000)
httpd = HTTPServer(server_address, serveur)
httpd.serve_forever()

