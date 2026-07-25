import socket

from src.fnix.networking.sync_manager import SyncManager
from src.fnix.networking.async_manager import AsyncManager


class Listener:
    def start_server(self, app):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        server_socket.bind(('localhost', 8080))
        server_socket.listen(5)

        print('server is launched on port :8080')

        try:
            if app.mode == "Async":
                manager = AsyncManager()
            else:
                manager = SyncManager()

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