import socket

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = '127.0.0.1'
    port = 12345
    server_socket.bind((host, port))
    server_socket.listen(1)
    print("Server listening on {}:{}".format(host, port))

    conn, addr = server_socket.accept()
    print("Connected to client: {}".format(addr))

    while True:
        data = conn.recv(1024).decode()
        if not data:
            break
        print("Received message from client: {}".format(data))
        response = "Server received: {}".format(data)
        conn.sendall(response.encode())

    conn.close()

if __name__ == "__main__":
    start_server()
