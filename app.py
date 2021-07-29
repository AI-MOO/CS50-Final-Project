import os
from flask import Flask, flash, redirect, render_template, request

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.route("/", methods=["GET","POST"])
def home():
    return render_template("home.html")


@app.route("/home", methods=["GET","POST"])
def home1():
    return render_template("home.html")


@app.route("/about", methods=["GET","POST"])
def about():
    return render_template("about.html")


@app.route("/contact", methods=["GET","POST"])
def contact():
    return render_template("contact.html")


@app.route("/books", methods=["GET","POST"])
def books():
    return render_template("books.html")


@app.route("/projects", methods=["GET","POST"])
def projects():
    return render_template("projects.html")

if __name__ == '__main__':
    app.run()