import socket
import threading
from time import sleep


def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = '127.0.0.1'
    port = 12345

    client_socket.connect((host, port))
    client_socket.settimeout(2)
    ping = "PING from client"
    client_socket.sendall(ping.encode())
    
    # response = client_socket.recv(1024).decode()
    # print("Server response: {}".format(response))

    # sleep(1)

def inputRFID(client_socket):
    while True:
        message = input("Enter a message : ")
        if message.lower() == 'exit':
            break
            
        client_socket.sendall(message.encode())

        response = client_socket.recv(1024).decode()
        print("Server response: {}".format(response))


if __name__ == "__main__":
    start_client()
