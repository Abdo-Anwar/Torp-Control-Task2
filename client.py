import socket

ip = input("Enter server IP address: ")
PORT = int(input("Enter server port: "))

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((ip, PORT))

while True:
    command = input('Enter "get" to retrieve files, "post" to upload, or "exit" to exit: ').lower()
    
    if command == "get" or command == "post" or command == "exit":
        client_socket.send(command.encode())
        if command == 'exit':
            break
        response = client_socket.recv(1024).decode()
        print(f"Server response: {response}")
    else:
        print("Invalid input. Please try again.")

client_socket.close()
