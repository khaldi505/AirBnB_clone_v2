#!/usr/bin/python3
"""
a script that starts a flask web application
"""


from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ returns Hello hbnb!"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ returns Hello hbnb!"""

    return "HBNB"


if __name__ == '__main__':
    app.run()
