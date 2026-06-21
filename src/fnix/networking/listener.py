import socket
from src.fnix.core.application import Application
from src.fnix.core.handlers import index_handler
from src.fnix.core.handlers import about_handler
from thread_manager import ThreadManager
from connection import Connection


class Listener:
    def start_server(self):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        server_socket.bind(('localhost', 8080))
        server_socket.listen(5)

        print('server is launched on port :8080')

        try:
            app = Application()

            app.add_route("/", index_handler)
            app.add_route("/about", about_handler)

            manager = ThreadManager()

            while True:
                client_socket, client_address = server_socket.accept()

                manager.handle(
                    client_socket,
                    client_address,
                    app
                )

        except KeyboardInterrupt:
            server_socket.close()


if __name__ == "__main__":
    Listener().start_server()