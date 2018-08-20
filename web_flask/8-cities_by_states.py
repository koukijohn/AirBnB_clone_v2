#!/usr/bin/python3
"""
    This is a script that starts a Flask web application and will display:
    / will display "Hello HBNB!", /hbnb will display "HBNB", /c/<text>
    will display "C " followed by value of the text variable w/out a space,
    /python/<text> will display "Python ", followed by value of text variable.
    /number/<n> will display "n is a number" only if n is an integer.
    /number_template/<n> will display a HTML page only if n is an integer
          H1 tag: "Number: n" inside the tag BODY
    /number_odd_or_even/<n> will display a HTML page only if n is an integer
          H1 tag: "Number: n is even|odd" inside the tag BODY
"""
from flask import Flask, render_template
import models
from models.city import City
from models.state import State
from models.amenity import Amenity
from models.user import User
from models.place import Place
from models.review import Review
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


@app.route('/number_odd_or_even/<int:n>')
def is_number_odd_or_even(n):
    return render_template("6-number_odd_or_even.html", n=n,
                           balance="even" if n % 2 == 0 else "odd")


@app.route('/states_list')
def display_states_list():
    all_state = models.storage.all(State).items()
    result = []
    for k, v in all_state:
        result.append((parse_id(k), v.name))
    result.sort(key=lambda tup: tup[1])
    return render_template("7-states_list.html", state_dict=result)


@app.route('/cities_by_states')
def display_city_list():
    all_state = models.storage.all(State).items()
    all_city = models.storage.all(City).items()
    result = []
    for k, v in all_state:
        city_result = []
        for a, b in all_city:
            if v.id == b.state_id:
                city_result.append((parse_id(a), b.name))
                city_result.sort(key=lambda tup: tup[1])
        result.append((parse_id(k), v.name, city_result))
        result.sort(key=lambda tup: tup[1])
    return render_template("8-cities_by_states.html", state_dict=result)


@app.teardown_appcontext
def teardown_cntx(err):
    models.storage.close()


def parse_id(string_id):
    id_portion = string_id.split('.')[1]
    return (id_portion)


if __name__ == "__main__":
    app.run()
