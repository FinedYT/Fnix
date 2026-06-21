from src.fnix.http.parser import HTTPParser
from src.fnix.http.response import Response
from src.fnix.http.response_builder import ResponseBuilder
from src.fnix.core.template_loader import TemplateLoader
from src.fnix.core.static_loader import StaticLoader

class Connection:

    def __init__(self, client_socket, client_address, app):
        self.client_socket = client_socket
        self.client_address = client_address
        self.app = app
        self.parser = HTTPParser()

    def handle(self):
        print(f"Client connected: {self.client_address}")

        try:

            data = self.client_socket.recv(1024)

            request = self.parser.parse(data)
            for middleware in self.app.middlewares:
                middleware.before_request(request)

            if request.path.startswith("/static/"):
                file_path = request.path.replace("/static/", "")

                content, mime = StaticLoader.load(file_path)

                response = Response()
                response.body = content.decode("utf-8")
                response.headers = {"Content-Type": mime}

                builder = ResponseBuilder()
                http_response = builder.build(response)

                self.client_socket.sendall(http_response.encode("utf-8"))

                return

            handler = self.app.router.resolve(request.method, request.path)

            if handler:
                response = handler(request)
            else:
                response = Response()
                response.status_code = 404
                response.status_text = "Not Found"
                response.body = TemplateLoader.load_template("404.html")

            for middleware in self.app.middlewares:
                middleware.after_request(request, response)

            print(f" Method: {request.method}\n Path: {request.path}\n Version: {request.version}")

            builder = ResponseBuilder()

            http_response = builder.build(response)

            self.client_socket.sendall(
                http_response.encode("utf-8")
            )

        except Exception as err:
            print(f"Connection error: {err}")

        finally:
            self.client_socket.close()
            print(f"Client disconnected: {self.client_address}")
