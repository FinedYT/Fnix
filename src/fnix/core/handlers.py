from src.fnix.http.response import Response

response = Response()

def index_handler():
    with open("src/fnix/templates/index.html", encoding="utf-8") as f:
        response.body = f.read()
    return response

def about_handler():
    with open("src/fnix/templates/about.html", encoding="utf-8") as f:
        response.body = f.read()
    return response