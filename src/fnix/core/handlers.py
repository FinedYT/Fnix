from src.fnix.http.response import Response
from src.fnix.core.template_loader import TemplateLoader

response = Response()

def index_handler():
    response.body = TemplateLoader.load_template("index.html")
    return response

def about_handler():
    response.body = TemplateLoader.load_template("about.html")
    return response