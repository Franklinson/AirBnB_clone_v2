#!/usr/bin/python3
"""
Web application based on flask
"""

from flask import Flask

app = Flask(__name__)


# Route definition with strict_slashes=False
@app.route('/', strict_slashes=False)
def hello_hbnb():
    """welcome page"""
    return "Hello HBNB!"


# Second page for web app
@app.route('/hbnb', strict_slashes=False)
def display_hbnb():
    """display route with hbnb"""
    return "HBNB"


# Third page for web app
@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """Takes a variable from the route"""
    formatted_text = text.replace('_', ' ')
    return f"C {formatted_text}"


# Set a default variable for text
@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text="is cool"):
    """Takes variable from the route or remain default"""
    text = text.replace('_', ' ')
    return f"Python {text}"


# Set route to accept only int variables
@app.route('/number/<int:n>', strict_slashes=False)
def is_number(n):
    """Accepts only int number from route"""
    return f'{n} is a number'


if __name__ == '__main__':
    # Run the Flask app on 0.0.0.0 and port 5000
    app.run(host='0.0.0.0', port=5000)
