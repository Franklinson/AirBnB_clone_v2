#!/usr/bin/python3
"""Script to start a Flask web application"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def teardown_appcontext(self):
    """remove application context"""
    storage.close()


@app.route("/states_list", strict_slashes=False)
def display_states():
    """Render state_list html page to display States created"""
    states = storage.all()
    return render_template('7-states_list.html', states=states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
