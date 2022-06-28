# Getting Started with Flask
from flask import Flask, redirect, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Hello, World!</h1>'


@app.route('/<name>')
def greet(name):
    return "Hello, %s" %name
    # return f"Hello, {name}"

# @app.route('/admin/')
@app.route('/admin')
def admin():
    return redirect(url_for("home"))
    

if __name__ == ("__main__"):
    app.run()
