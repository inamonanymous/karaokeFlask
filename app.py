from flask import Flask, render_template, request
from cs50 import SQL

app = Flask(__name__)
db = SQL("sqlite:///songlist.db")

@app.route("/")
def index():
    return render_template("/index.html")

@app.route("/search", methods=["GET"])
def search():
    #query = str(request.args.get('q'))
    song = db.execute('SELECT * FROM songlist WHERE title LIKE ? ORDER BY title ASC', '%' + request.args.get('q') + '%')
    return render_template("/search.html", songlist=song)

@app.route("/index", methods=["POST"])
def welcome():
    isClicked = "submit_clicked" in request.form
    if not isClicked:
        return render_template("/index.html")
    return render_template("/welcome.html", submitClicked=isClicked)