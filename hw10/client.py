import socket
import os

# Client
# By Randy Dickersbach

host = 'localhost'
port = 9999

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((host, port))  # Establishes the Connection

user_input = input("Enter Message (pwd, ls, cd, mkdir, rm, write, cat, quit: ")
client_socket.send(user_input.encode())
if user_input == "quit":
    client_socket.close()
    quit(0)
if user_input[:5] == "write":
    user = input("Write inside the folder: ")
    client_socket.send(user.encode())
msg_from_server = client_socket.recv(4096).decode()
print(msg_from_server)

client_socket.close()