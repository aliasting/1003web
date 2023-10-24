from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.jinja.html")

@app.route("/flask_web")
def hello_world():
    return "<h1>flask web.</h1>"