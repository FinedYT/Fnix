from connection import Connection
from manager import ConnectionManager

class SyncManager(ConnectionManager):
    def handle(self, client_socket, client_address, app):
        conn = Connection(
            client_socket,
            client_address,
            app
        )
        conn.handle()