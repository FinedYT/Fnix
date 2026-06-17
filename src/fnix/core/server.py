from src.fnix.core.application import Application

app = Application()

app.add_route("/")
def home():
    return "hello"

app.add_route("/about")
def about():
    return "hello2"