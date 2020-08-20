import pandas as pd
import random
from flask import Flask, render_template, request

raw = (pd.read_excel("https://github.com/busgandy/gideonbusayo/blob/master/ranking.xlsx?raw=true"))


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/hello")
def hello():
    name = request.args.get("name")
    hello = raw.loc[raw['Student ID'] == name]
    if not name:
        render_template("failure.html)
    for items in hello:
        if name != items:
            render_template("failure.html)
    return render_template("hello.html", hello = name)
