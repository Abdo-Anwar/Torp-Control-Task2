import socket as sk
#local ip = '192.168.1.15'
#port = 12345
ip = input("Enter ip address: ")
PORT = int(input("Enter sever port: "))


client_socket = sk.socket(sk.AF_INET, sk.SOCK_STREAM)
client_socket.connect((ip,PORT))

while True:
    data= input("Enter Data or 'exit' to exit: ")
    client_socket.sendall(data.encode())  
    if data.lower() == 'exit':
        break
    receivedData=client_socket.recv(1024) 
    print(f"Data received from server is {receivedData.decode()}")
client_socket.close() 