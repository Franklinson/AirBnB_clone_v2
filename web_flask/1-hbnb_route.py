#!/usr/bin/python3
"""
Adding a route to the previous codes
"""

from flask import Flask

app = Flask(__name__)


# Route definition with strict_slashes=False
@app.route('/', strict_slashes=False)
def hello_hbnb():
    return "Hello HBNB!"


# Second page for
@app.route('/hbnb', strict_slashes=False)
def display_hbnb():
    return "HBNB"


if __name__ == '__main__':
    # Run the Flask app on 0.0.0.0 and port 5000
    app.run(host='0.0.0.0', port=5000)
