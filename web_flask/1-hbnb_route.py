#!/usr/bin/python3
"""
    This is a script that starts a Flask web application and will display:
    / will display “Hello HBNB!” and /hbnb will display “HBNB”.
"""
from flask import Flask
app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"


if __name__ == "__main__":
    app.run()
