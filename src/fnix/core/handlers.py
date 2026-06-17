from src.fnix.http.response import Response
from src.fnix.core.template_loader import TemplateLoader

def index_handler():
    response = Response()
    response.body = TemplateLoader.load_template("index.html")
    return response

def about_handler():
    response = Response()
    response.body = TemplateLoader.load_template("about.html")
    return response