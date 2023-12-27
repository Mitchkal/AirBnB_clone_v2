#!/usr/bin/python3
"""
module 2-c_route.py
"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    returns "Hello HBNB"
    """
    return ("Hello HBNB")


@app.route('/hbnb', strict_slashes=False)
def display_hbnb():
    """
    returns "HBNB"
    """
    return ("HBNB")


@app.route('/c/<text>', strict_slashes=False)
def display_c(text):
    """
    returns c followed by text var
    """
    text_with_spaces = text.replace('_', ' ')
    return ('C {}'.format(text_with_spaces))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
