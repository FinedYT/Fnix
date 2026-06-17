import socket
from src.fnix.core.application import Application
from src.fnix.core.handlers import index_handler
from src.fnix.core.handlers import about_handler
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
            app = Application()

            app.add_route("/", index_handler)
            app.add_route("/about", about_handler)

            while True:
                client_socket, client_address = server_socket.accept()

                conn = Connection(
                    client_socket,
                    client_address,
                    app
                )

                conn.handle()

        except KeyboardInterrupt:
            server_socket.close()


if __name__ == "__main__":
    Listener().start_server()