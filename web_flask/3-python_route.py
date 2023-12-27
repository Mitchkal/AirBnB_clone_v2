#!/usr/bin/python3
"""
module 3-python_route
"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    returns "hello hbnb"
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
    returns c followed by text
    """
    text_with_spaces = text.replace('_', ' ')
    return ('C {}'.format(text_with_spaces))


@app.route('/python/<text>', strict_slashes=False)
@app.route('/python/', strict_slashes=False)
def display_text(text="is cool"):
    """
    displays with and without input text
    """
    text_with_space = text.replace('_', ' ')
    return ('Python {}'.format(text_with_space))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
