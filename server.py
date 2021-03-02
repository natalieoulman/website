"""Server for Natalie's website."""

from flask import Flask, render_template, request, session, jsonify
# from model import connect_to_db

app = Flask(__name__)

#============================     PAGE ROUTES    ==================================#


@app.route("/")
def my_index():
    """Rendering landing page for Natalie's site"""

    return render_template("index.html")


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
