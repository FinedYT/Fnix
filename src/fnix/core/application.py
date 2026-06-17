from src.fnix.routing.router import Router

class Application:
    def __init__(self):
        self.router = Router()
        self.middlewares = []
    def add_route(self, path, handler):
        self.router.add_route(path, handler)
    def add_middleware(self, middleware):
        self.middlewares.append(middleware)