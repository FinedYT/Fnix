import socket
from connection import Connection


class Listener:
    def start_server(self):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        server_socket.bind(('localhost', 8080))
        server_socket.listen(5)

        print('Listening on port 8080')
        print('server is launched on 127.0.0.1:8080')

        try:
            while True:
                client_socket, client_address = server_socket.accept()

                conn = Connection(client_socket, client_address)
                conn.handle()

        except KeyboardInterrupt:
            server_socket.close()


if __name__ == "__main__":
    Listener().start_server()