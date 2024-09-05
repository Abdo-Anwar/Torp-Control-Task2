import socket
import threading

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
        data = client_socket.recv(1024)
        if not data:
            break
        message = data.decode()
        if message.lower() == 'exit':
            print(f"Client {client_address} disconnected")
            client_num -= 1
            if client_num == 0:
                server_running = False
            break
        else:
            print(f"Received from {client_address}: {message}")
            client_socket.send(data) 
    client_socket.close()
    


try:
    while server_running:
        client_socket, client_address = server_socket.accept()
        client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_thread.start()
finally:
    server_socket.close()

    