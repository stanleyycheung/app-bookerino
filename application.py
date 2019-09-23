import os

from flask import Flask, session, render_template, request, redirect, url_for
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

import requests

API_KEY = "9if6Tul5OHosGNcHcNSNVw"
app = Flask(__name__)

res = requests.get("https://www.goodreads.com/book/review_counts.json",
                   params={"key": API_KEY, "isbns": "9781632168146"})
print(res.json())

# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))


@app.route("/")
def index():
    return "Hello World"


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        return redirect("/")
    else:
        return render_template("login.html")
