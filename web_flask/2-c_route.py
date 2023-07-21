#!/usr/bin/python3

"""
flask model for route
"""
from flask import Flask

app = Flask(__name__)

"""Route defination with strict_slashes=False"""


@app.route('/', strict_slashes=False)
def hello():
    """ prints HELLO HBNB """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ prints HBNB"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """ prints text """
    text = text.replace('_', ' ')
    return f'C {text}'


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
