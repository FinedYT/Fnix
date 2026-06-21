from threading import Thread
from .connection import Connection
from .manager import ConnectionManager

class ThreadManager(ConnectionManager):
    def handle(self, client_socket, client_address, app):
        conn = Connection(client_socket, client_address, app)

        Thread(target=conn.handle).start()