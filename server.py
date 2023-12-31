#!/usr/bin/env python
import http.server
import ssl
import socketserver

cert_file = "./localhost.pem"
key_file = "./localhost-key.pem"

class RequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Cache-Control", "no-cache, no-store, must-revalidate")
        self.send_header("Pragma", "no-cache")
        self.send_header("Expires", "0")
        super().end_headers()

httpd = socketserver.TCPServer(
    ('', 8080),
    RequestHandler
)

httpd.socket = ssl.wrap_socket(
    httpd.socket,
    server_side=True,
    keyfile=key_file,
    certfile=cert_file
)

httpd.serve_forever()
