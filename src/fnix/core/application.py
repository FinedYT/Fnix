from src.fnix.routing.router import Router

class Application:
    def __init__(self):
        self.router = Router()

    def add_route(self, path, handler):
        self.router.add_route(path, handler)