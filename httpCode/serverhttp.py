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
        #full_file_path = os.path.join(UPLOAD_DIR, file_path)

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



    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode('utf-8')
        post_params = parse_qs(post_data)

         # Save the uploaded file (assuming form field is 'file')
        file_content = post_params.get('file', [None])[0]
        if file_content:
            file_path = os.path.join(UPLOAD_DIR, "uploaded_file.txt")  # Save to UPLOAD_DIR
            with open(file_path, "w") as f:
                f.write(file_content)
            
            # Respond with acknowledgment
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"File uploaded successfully!")
        else:
            # No file found in the POST request
            self.send_response(400)
            self.end_headers()
            self.wfile.write(b"Bad Request: No file uploaded.")


def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler, port=12345):
    server_address = ('', port) # '' The empty string means the server will listen on all available IP addresses
    httpd = server_class(server_address, handler_class)
    print(f'Starting server on port {port}...')
    httpd.serve_forever()

if __name__ == '__main__':
    run()