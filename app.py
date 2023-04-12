from flask import Flask, render_template, request
from cs50 import SQL

app = Flask(__name__)
db = SQL("sqlite:///songlist.db")

@app.route("/")
def index():
    return render_template("/index.html")

@app.route("/search", methods=["GET"])
def search():
    q = request.args.get("q")
    if q:
        song = db.execute("SELECT * FROM songlist WHERE title LIKE ? LIMIT 50", "%" + q + "%")
    else:
        song = []
    return render_template("search.html", songlist=song)

@app.route("/index", methods=["POST"])
def welcome():
    if not "submit_clicked" in request.form:
        return render_template("/index.html")
    return render_template("/welcome.html")