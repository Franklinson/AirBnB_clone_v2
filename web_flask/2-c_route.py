#!/usr/bin/python3
"""
Adding a route to the previous codes to accept variables
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


# Third page for web app
@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    formatted_text = text.replace('_', ' ')
    return f"C {formatted_text}"


if __name__ == '__main__':
    # Run the Flask app on 0.0.0.0 and port 5000
    app.run(host='0.0.0.0', port=5000)
