import socket

#Client
#By Randy Dickersbach

host = 'localhost'
port = 9999

client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client_socket.connect((host, port)) #Establishes the Connection
while True:
    user_input = input("Enter Message: ")
    client_socket.send(user_input.encode())
    if(user_input == 'quit'):
        break
    msg_from_server =client_socket.recv(4096)
    print(msg_from_server.decode())

client_socket.close()
