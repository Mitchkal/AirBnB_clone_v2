#!/usr/bin/python3
"""
module 5-number_template
"""
from flask import Flask, abort, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def display_hello():
    """displays hello hbnb"""
    return ("Hello HBNB!")


@app.route('/hbnb', strict_slashes=False)
def display_hbnb():
    """displays HBNB"""
    return ("HBNB")


@app.route('/c/<text>', strict_slashes=False)
def display_c(text):
    """displays text with spaces"""
    text_with_space = text.replace('_', ' ')
    return ('C {}'.format(text_with_space))


@app.route('/python/(<text>)', strict_slashes=False)
@app.route('/python/', strict_slashes=False)
def display_python(text='is cool'):
    """displays with or without custom text"""
    text_with_spaces = text.replace('_', ' ')
    return ('Python {}'.format(text_with_spaces))


@app.route('/number/<n>', strict_slashes=False)
def display_if_int(n):
    """displays if input n is an integer"""
    try:
        n = int(n)
        return ('{} is an integer'.format(n))
    except Exception as e:
        abort(404)


@app.route('/number_template/<n>', strict_slashes=False)
def number_template(n):
    """displays html page if n is integer"""
    try:
        n = int(n)
        return (render_template('5-number.html', Number=n))
    except Exception as e:
        abort(404)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
