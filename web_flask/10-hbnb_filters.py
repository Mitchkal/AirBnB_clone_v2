#!/usr/bin/python3
"""
module 10 hbnb filters
"""
from flask import Flask, render_template, abort
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity


app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def states():
    """displays cities by states"""
    states = sorted(storage.all(State).values(), key=lambda x: x.name)
    cities = sorted(storage.all(City).values(), key=lambda x: x.name)
    amenities = sorted(storage.all(Amenity).values(), key=lambda x: x.name)

    return render_template('10-hbnb_filters.html', states=states,
                           cities=cities, amenities=amenities)


"""@app.route('/hbnb_filters', strict_slashes=False)
def state_detail(id):
    displays state details
    states = storage.all(State).values()
    state = next((state for state in states if state.id == id), None)
    if state:
        cities = sorted(state.cities, key=lambda x: x.name) if state else []
        return render_template('10-hbnb_filter.html',
        state=state, cities=cities)
    else:
        return render_template('9-states.html', states=None)"""


@app.teardown_appcontext
def teardown_appcontext(exception):
    """closes context"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
