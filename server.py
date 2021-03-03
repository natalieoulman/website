"""Server for Natalie's website."""

from flask import Flask, render_template, request, flash, session, redirect
from jinja2 import StrictUndefined
import requests
import json
app = Flask(__name__)

#============================     PAGE ROUTES    ==================================#


@app.route('/')
def homepage():
    """Rendering landing page for Natalie's site"""

    return render_template("index.html")


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
