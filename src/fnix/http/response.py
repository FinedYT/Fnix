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