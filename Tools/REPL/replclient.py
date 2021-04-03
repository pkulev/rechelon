from socket import socket, AF_INET, SOCK_DGRAM


class Client:

    def __init__(self, connection):
        self.connection = connection

    def execute(self, command):
        self.connection.sendall(str(command))
        return self.connection.recv(1024)

    def close(self):
        self.connection.close()

def connect(host="localhost", port=27450):
    """Connect to server."""

    client = socket(AF_INET, SOCK_DGRAM)
    client.connect((host, port))

    return client