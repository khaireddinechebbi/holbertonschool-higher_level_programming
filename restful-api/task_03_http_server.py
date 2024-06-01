#!/usr/bin/python3
"""
"""
import http.server
import socketserver
import json

PORT = 8080
class SimpleHTTPRequestHandler(http.server.BaseHTTPRequestHandler):
    """
    """
    def do_GET(self):
        """
        """
        if self.path == "/":
            self.send_response(200)
            self.wfile.write(b"Hello, this is a simple API!")
        elif self.path == "\data":
            self.send_response(200)
            dataset = {"name": "John", "age": 30, "city": "New York"}
            self.wfile.write(json.dumps(dataset))
        elif self.path == "\status":
            self.send_response(200)
            return "ok"
        else:
            self.send_response(404)
            return "404 Not Found"
    
with socketserver.TCPServer(("", PORT), SimpleHTTPRequestHandler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()