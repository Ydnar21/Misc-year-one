import socket
#Server
#By Randy Dickersbach




#FIX this
import threading

from echo_client import client_socket

port =9999

def handle(): #thread
    while True:
        msg_from_client= client_socket.recv(4096)
        if msg_from_client == 'quit':
            break
        upper_case =msg_from_client.decode().upper()
        client_socket.send(upper_case.encode()) # Can not just send a message it must be encoded to bytes (can use .encode)


def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # IPv4 they are both defaults
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # Can reuse the address immediately
    server_socket.bind(("", port))  # Just a string can allow anyone to connect to you
    server_socket.listen()
    print("Server is Listening.")
    while True:
        (client_socket, client_address) = server_socket.accept()  # blocking
        thread = threading.Thread(target= handle, args= (client_socket,))
        client_socket.close()
        print(f'Got connection from this {client_address}')

if __name__ == '__main__':
    main()