#!/usr/bin/python3
from flask import Flask, render_template
app = Flask(__name__)

app.url_map.strict_slashes = False

@app.route('/')
def hello_hbnb():
    return "Hello HBNB!"

@app.route('/hbnb')
def hbnb():
    return "HBNB"

@app.route('/c/<text>')
def display_c(text):
    return "C {}".format(text).replace("_", " ")


@app.route('/python/')
@app.route('/python/<text>')
def display_python(text="is cool"):
    return "Python {}".format(text).replace("_", " ")

@app.route('/number/<int:n>')
def display_number(n):
    return "{} is a number".format(n)

@app.route('/number_template/<int:n>')
def display_html_if_num(n):
    return render_template("5-number.html", n=n)


app.run()
