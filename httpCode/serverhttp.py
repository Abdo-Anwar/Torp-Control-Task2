from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs
import os


#handel directory to store files

UPLOAD_DIR = 'Files_Uploads'
if not os.path.exists(UPLOAD_DIR):
    os.makedirs(UPLOAD_DIR)