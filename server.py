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

    return render_template("home.html")


@app.route('/natalie-projects')
def project():
    """Rendering project page for Natalie's site"""

    return render_template("projects.html")


@app.route('/natalie-about')
def about():
    """Rendering about page for Natalie's site"""

    return render_template("about.html")


@app.route('/natalie-contact')
def contact():
    """Rendering contact page for Natalie's site"""

    return render_template("contact.html")


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
