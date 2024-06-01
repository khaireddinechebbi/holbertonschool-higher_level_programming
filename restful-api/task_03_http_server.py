#!/usr/bin/python3
"""
A simple HTTP server using http.server module to demonstrate basic web server functionality.
"""

import http.server
import json
from http.server import HTTPServer


class SimpleHTTPRequestHandler(http.server.BaseHTTPRequestHandler):
    """
    A simple HTTP request handler that serves different types of responses for various endpoints.
    """

    def do_GET(self):
        """
        Handle GET requests to serve different endpoints with appropriate responses.
        """
        if self.path == "/":
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")
        elif self.path == "/data":
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            dataset = {"name": "John", "age": 30, "city": "New York"}
            self.wfile.write(json.dumps(dataset).encode('utf-8'))
        elif self.path == "/status":
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            status = {"status": "OK"}
            self.wfile.write(json.dumps(status).encode('utf-8'))
        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"Endpoint not found")


if __name__ == "__main__":
    """
    Run the server on port 8000
    """
    httpd = HTTPServer(('', 8000), SimpleHTTPRequestHandler)
    print(f"Serving on port 8000")
    httpd.serve_forever()
