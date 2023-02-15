# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 10:24:35 2023

@author: gtaus
"""

from flask import Flask
from gevent.pywsgi import WSGIServer
from flask import request, escape


app = Flask(__name__)

@app.route("/")

def index():
    celsius = request.args.get("celsius", "")
    if celsius:
        fahrenheit = fahrenheit_from(celsius)
    else:
        fahrenheit = ""
    return (
        """<form action="" method="get">
                Celsius temperature: <input type="text" name="celsius">
                <input type="submit" value="Convert to Fahrenheit">
            </form>"""
        + "Fahrenheit: "
        + fahrenheit
    )

def fahrenheit_from(celsius):
    """Convert Celsius to Fahrenheit degrees."""
    try:
        fahrenheit = float(celsius) * 9 / 5 + 32
        fahrenheit = round(fahrenheit, 3)  # Round to three decimal places
        return str(fahrenheit)
    except ValueError:
        return "invalid input"

@app.route("/<int:celsius>")

# def hello():
    # return "Hello World"

def fahrenheit_from(celsius):
    """Convert Celsius to Fahrenheit degrees."""
    fahrenheit = float(celsius) * 9 / 5 + 32
    fahrenheit = round(fahrenheit, 3)  # Round to three decimal places
    return str(fahrenheit)




if __name__ == "__main__":
    # from waitress import serve
    # serve(app, host="0.0.0.0", port=8080)
    # serve(app,host='https://localhost:5000/')
    http_server = WSGIServer(('127.0.0.1', 5000), app)
    http_server.serve_forever()
    app.run(debug=True)