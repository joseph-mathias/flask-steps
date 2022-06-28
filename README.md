# flask-steps
Flask is a web application framework written in Python. It was developed by Armin Ronacher, who led a team of international Python enthusiasts called Poocco. Flask is based on the Werkzeg WSGI toolkit and the Jinja2 template engine.Both are Pocco projects A Minimal Application

##A minimal Flask application looks something like this:
```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
```
_So what did that code do?_

    First we imported the Flask class. An instance of this class will be our WSGI application.

    Next we create an instance of this class. The first argument is the name of the application’s module or package. __name__ is a convenient shortcut for this that is appropriate for most cases. This is needed so that Flask knows where to look for resources such as templates and static files.

    We then use the route() decorator to tell Flask what URL should trigger our function.

    The function returns the message we want to display in the user’s browser. The default content type is HTML, so HTML in the string will be rendered by the browser.
