#!/usr/bin/python3
# a script that starts a flask web application


from flask import Flask


app = Flask(__name__)


app.url_map.strict_slashes = False
@app.route('/')
def hello_hbnb():
	""" returns Hello hbnb!"""

	return "Hello HBNB!"

if __name__ == '__main__':
   app.run()
