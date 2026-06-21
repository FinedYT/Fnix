from src.fnix.routing.router import Router
from src.fnix.networking.listener import Listener

class Application:
    def __init__(self):
        self.router = Router()
        self.middlewares = []
        self.mode = "sync"

    def run(self, mode="sync"):
        self.mode = mode
        Listener().start_server(self)

    def route(self, path):
        def decorator(handler):
            self.add_route(path, handler)
            return handler

        return decorator

    def get(self, path):
        def decorator(handler):
            self.router.add_route(path, handler, method="GET")
            return handler

        return decorator

    def post(self, path):
        def decorator(handler):
            self.router.add_route(path, handler, method="POST")
            return handler
        return decorator

    def add_route(self, path, handler):
        self.router.add_route(path, handler)

    def add_middleware(self, middleware):
        self.middlewares.append(middleware)