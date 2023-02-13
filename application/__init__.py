from flask import Flask
from dotenv import load_dotenv
from application.routes import index
from application.views import user


app = Flask(__name__)
load_dotenv()

app.add_url_rule(
    "/",
    view_func=index.Index.as_view("index")
)

# Assign comics to an user
app.add_url_rule(
    rule='/addToLayaway',
    methods=['POST'],
    view_func=user.AsignComic.as_view('addToLayaway')
)