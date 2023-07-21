#!/usr/bin/python3

"""
flask model for route
"""
from flask import Flask

app = Flask(__name__)


"""Route defination with strict_slashes=False"""


@app.route('/', strict_slashes=False)
def hello():
    """ prints Hello HBNB """
    return 'Hello HBNB!'


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
