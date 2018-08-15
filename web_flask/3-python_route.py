#!/usr/bin/python3
"""
    This is a script that starts a Flask web application and will display:
    / will display “Hello HBNB!”, /hbnb will display “HBNB”, /c/<text>
    will display “C ” followed by value of the text variable w/out a space,
    /python/<text> will display “Python ”, followed by value of text variable.
"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def display_c(text):
    return "C {}".format(text).replace("_", " ")


@app.route('/python/')
@app.route('/python/<text>', strict_slashes=False)
def display_python(text="is cool"):
    return "Python {}".format(text).replace("_", " ")


if __name__ == "__main__":
    app.run()
