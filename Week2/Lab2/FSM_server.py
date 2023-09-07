import socket
import os
import subprocess

port =9999


def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # IPv4 they are both defaults
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # Can reuse the address immediately
    server_socket.bind(("", port))  # Just a string can allow anyone to connect to you
    server_socket.listen()
    print("Server is Listening.")
    # thread = threading.Thread(target= handle, args= (client_socket,))
    (client_socket, client_address) = server_socket.accept()  # blocking
    print(f'Got connection from this {client_address}')
    while True:
        msg_from_client = client_socket.recv(4096).decode()
        print(msg_from_client)
        if msg_from_client == "quit" or msg_from_client== "pwd" or msg_from_client == "ls" or msg_from_client[0:5] == "mkdir" or msg_from_client[0:2] == "rm" or msg_from_client[0:5] == "write" or msg_from_client[0:2] == "cd" or msg_from_client[0:3]=="cat":
            if msg_from_client == "quit":
                msg = "quit"
                exit(0)
            if msg_from_client == "pwd":
                msg = os.getcwd()
            if msg_from_client == "ls":
                listToStr = ' '.join([str(elem) for elem in os.listdir(os.curdir)])
                print(listToStr)
                msg = listToStr
            if msg_from_client[0:5] == "mkdir":
                os.mkdir(msg_from_client[6:])
                msg = msg_from_client[6:] + " " + "was created"
            if msg_from_client[0:2] == "rm":
                #os.removedirs(msg_from_client[3:])
                os.rmdir(msg_from_client[3:])
                msg = msg_from_client[3:] + " " + "was removed"
            if msg_from_client[0:5] == "write":
                try:
                    fd = os.open(msg_from_client[6:],os.O_RDWR|os.O_CREAT|os.O_APPEND)
                    text_msg_from_client = client_socket.recv(4096).decode()
                    print(text_msg_from_client)
                except Exception:
                    print("File was not found so a file was created")
                os.write(fd, text_msg_from_client.encode())
                msg = text_msg_from_client
                print(msg)
            if msg_from_client[0:2] == "cd":
                print(msg_from_client[3:])
                try:
                    os.chdir(msg_from_client[3:])
                    msg = "Changed dir " + msg_from_client[2:]
                except WindowsError:
                    msg = "Directory is not valid"
                    client_socket.send(msg.encode())
                except Exception as e:
                    print(str(e))
            if msg_from_client[0:3] == "cat":
                try:
                    file =os.open(msg_from_client[4:],os.O_RDONLY)
                    msg = str(os.read(file,4069))
                    print(msg)
                    print(os.read(file,12))
                except FileNotFoundError:
                    print("File Does not exist")
            print("here")
            print(msg)
            client_socket.send(msg.encode())
        else:
            msg = "Invalid Command"
            client_socket.send(msg.encode())
    client_socket.close()



if __name__ == '__main__':
    main()