from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs
import os


#handel directory to store files

UPLOAD_DIR = 'Files_Uploads'
if not os.path.exists(UPLOAD_DIR):
    os.makedirs(UPLOAD_DIR)

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        file_path = self.path.lstrip('/')

        if file_path == '':  #  no path specified)
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(b'Hello, welcome to the server! (no path specified)')
        elif os.path.exists(file_path): #  Checks if the requested file exists on the server using
                self.send_response(200)
                self.send_header('Content-type', 'application/octet-stream')
                self.end_headers()
                with open(file_path, 'rb') as file:
                    self.wfile.write(file.read())

        else:  # File not found
                self.send_response(404)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(b'404 Not Found')