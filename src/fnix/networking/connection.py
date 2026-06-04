class Connection:
    def __init__(self, client_socket, client_address):
        self.client_socket = client_socket
        self.client_address = client_address

    def handle(self):
        print(f"Client connected: {self.client_address}")

        data = self.client_socket.recv(1024)

        print(data)

        self.client_socket.close()

        print(f"Client disconnected: {self.client_address}")