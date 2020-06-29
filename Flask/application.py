import datetime
from flask import Flask,render_template,request

app = Flask(__name__)
notes = [];

@app.route("/")
def index():
    return render_template("index.html",notes=notes)


@app.route("/hello",methods=["GET","POST"])
def hello():
    if request.method == "POST":
        note = request.form.get("enternote")
        notes.append(note)
    return render_template("hello.html",notes=notes)
