#!/usr/bin/python3
"""
    This is a script that starts a Flask web application and will display:
    / will display “Hello HBNB!”, /hbnb will display “HBNB”, and /c/<text>
    will display “C ” followed by value of the text variable w/out a space.
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

if __name__ == "__main__":
    app.run()
