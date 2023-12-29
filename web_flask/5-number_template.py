#!/usr/bin/python3
"""
module 4-number_route
"""
from flask import Flask, render_template, abort
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def display_hello():
    """displays Hello HBNB"""
    return ("Hello HBNB")


@app.route('/hbnb', strict_slashes=False)
def display_hbnb():
    """displays HBNB"""
    return ("HBNB")


@app.route('/c/<text>', strict_slashes=False)
def display_text(text):
    """displays text"""
    text_with_space = text.replace('_', ' ')
    return ('C {}'.format(text_with_space))


@app.route('/python/<text>', strict_slashes=False)
@app.route('/python', strict_slashes=False)
def display_c(text='is cool'):
    """
    returns text with default
    """
    text_with_spaces = text.replace('_', ' ')
    return ('Python {}'.format(text_with_spaces))


@app.route('/number/<n>', strict_slashes=False)
def test_integer(n):
    """displays if number is integer"""
    try:
        n = int(n)
        # if isinstance(n, int):
        return ('{} is a number'.format(n))
    except Exception as e:
        abort(404)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """displays html page if n is integer"""
    return (render_template('5-number.html', Number=n))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
