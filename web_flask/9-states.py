#!/usr/bin/python3
"""
module 8-number_route
"""
from flask import Flask, render_template, abort
from models import storage
from models.state import State
from models.city import City


app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def states():
    """displays cities by states"""
    states = storage.all(State).values()
    sorted_states = sorted(states, key=lambda x: x.name)
    return render_template('9-states.html', states=sorted_states)


@app.route('/states/<id>', strict_slashes=False)
def state_detail(id):
    """displays state details"""
    states = storage.all(State).values()
    state = next((state for state in states if state.id == id), None)
    if state:
        cities = sorted(state.cities, key=lambda x: x.name) if state else []
        return render_template('9-states.html', state=state, cities=cities)
    else:
        return render_template('9-states.html', states=None)


@app.teardown_appcontext
def teardown_appcontext(exception):
    """closes context"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
