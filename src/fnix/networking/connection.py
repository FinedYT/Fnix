from src.fnix.http.parser import HTTPParser


class Connection:
    def __init__(self, client_socket, client_address):
        self.client_socket = client_socket
        self.client_address = client_address
        self.parser = HTTPParser()

    def handle(self):
        print(f"Client connected: {self.client_address}")

        try:
            data = self.client_socket.recv(1024)

            request = self.parser.parse(data)

            print(f"Method: {request.method}")
            print(f"Path: {request.path}")
            print(f"Version: {request.version}")

        except Exception as err:
            print(f"Connection error: {err}")

        finally:
            self.client_socket.close()
            print(f"Client disconnected: {self.client_address}")