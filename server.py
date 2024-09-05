import socket
import threading
from httpCode import serverhttp as st

HOST = socket.gethostbyname(socket.gethostname())
PORT = 12345
server_running = True
client_num = 0

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(5)

def handle_client(client_socket, client_address):
    global server_running
    global client_num
    client_num += 1
    print(f"Connection from {client_address}")
    
    while True:
        data = client_socket.recv(1024).decode()
        print(data)
        if not data:
            break
        
        if data.lower() == 'exit':
            print(f"Client {client_address} disconnected")
            client_num -= 1
            if client_num == 0:
                server_running = False
            break
        elif data.lower() == 'get':
            handler = st.SimpleHTTPRequestHandler(client_socket, client_address, None)
            handler.do_GET()
        elif data.lower() == 'post':
            handler = st.SimpleHTTPRequestHandler(client_socket, client_address, None)
            handler.do_POST()
        else:
            client_socket.send(b"Invalid command")
    
    client_socket.close()
    

try:
    while server_running:
        client_socket, client_address = server_socket.accept()
        client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_thread.start()
finally:
    server_socket.close()