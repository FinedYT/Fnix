from src.fnix.http.response import Response

response = Response()

def home_handler():
    response.body = "home page"
    return response

def about_handler():
    response.body = "about page"
    return response