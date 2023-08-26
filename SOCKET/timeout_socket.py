import socket

# Create a socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Set a timeout of 5 seconds for socket operations
# timeout = 10
# client_socket.settimeout(timeout)

try:
    # Try to connect to a remote server
    client_socket.connect(("example.com", 80))

    # Send and receive data...
except socket.timeout:
    print("Connection or operation timed out.")
except socket.error as e:
    print(f"Socket error: {e}")
finally:
    client_socket.close()
