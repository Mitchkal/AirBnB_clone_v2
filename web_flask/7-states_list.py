#!/usr/bin/python3
"""
module 4-number_route
"""
from flask import Flask, render_template, abort
from models import storage
from models.state import State


app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def display_states():
    """displays states"""
    states = storage.all('State').values()
    sorted_states = sorted(states, key=lambda x: x.name)
    return render_template('7-states_list.html', states=sorted_states)


@app.teardown_appcontext
def teardown_appcontext(exception):
    """closes context"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0')
