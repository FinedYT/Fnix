from src.fnix.http.response import Response
from src.fnix.core.template_loader import TemplateLoader

def index_handler(request):
    response = Response()
    response.body = TemplateLoader.load_template("index.html")
    return response

def about_handler(request):
    response = Response()
    response.body = TemplateLoader.load_template("about.html")
    return response

def login_handler(request):
    response = Response()
    response.body = "Login OK"
    return response