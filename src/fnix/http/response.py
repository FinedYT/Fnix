import json

class Response:
    def __init__(self):
        self.status_code = 200
        self.status_text = "OK"
        self.headers = {
            "Content-Type": "text/html",
            "Server": "Fnix"
        }
        self.server = {"Server": "Fnix"}
        self.body = "<h1>Hello Fnix</h1>"

    @staticmethod
    def json(data):
        response = Response()
        response.body = json.dumps(data)
        response.headers = {"Content-Type": "application/json"}
        return response