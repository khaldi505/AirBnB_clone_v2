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


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """ returns c followed by a text """
    text = text.replace("_", " ")
    return 'C %s' % text


@app.route('/python/', defaults={'text': 'is cool'})
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    """
    returns python followed by a text
    if the input does not exist the default text is "is cool"
    """

    text = text.replace("_", " ")
    return 'Python %s' % text


@app.route('/number/<int:n>', strict_slashes=False)
def int_in(n):
    """ this will only returns an unsigned int """
    return '%i is a number' % n


if __name__ == '__main__':
    app.run()
