#!/usr/bin/python3
"""
"""
import http.server
import json

PORT = 8000


class SimpleHTTPRequestHandler(http.server.BaseHTTPRequestHandler):
    """
    """

    def do_GET(self):
        """
        """
        if self.path == "/":
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")
        elif self.path == "\\data":
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            dataset = {"name": "John", "age": 30, "city": "New York"}
            self.wfile.write(json.dumps(dataset))
        elif self.path == "\\status":
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"OK")
        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"404 Not Found")


httpd = HTTPServer(('', 8000), SimpleHTTPRequestHandler)
httpd.serve_forever()
