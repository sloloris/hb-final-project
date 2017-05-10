""" DESCRIPTION HERE """

from jinja2 import StrictUndefined

from flask_debugtoolbar import DebugToolbarExtension
from flask import Flask, jsonify, render_template, redirect, request, flash, session

from model import User, Contact, Relationship, ContactFrequency, Message, connect_to_db, db


app = Flask(__name__)

app.secret_key = "SOMETHINGHERE"

app.jinja_env.undefined = StrictUndefined #what does this do?


@app.route('/')
def index():
    """ Landing page. """

    return render_template("landing.html")


@app.route('/about')
def about():
    """ App about page. """

    return "about.html"


@app.route('/register')
def register():
    """ User account registration form. """

    return render_template('registration.html')


@app.route('/login', methods=["GET"])
def render_login_form(): # can I do this on the front end?
    """ Renders login form. """

    return render_template("login.html")


@app.route('/login', methods=["POST"])
def login_user():
    """ Initiates new Flask session for user. """

    return redirect("/login")


@app.route('/<user_id>/account')
def show_user_account_home(user_id):
    """ Renders user account homepage. """

    return render_template("user_account.html")


@app.route('/<user_id>/preferences')
def user_preferences(user_id):
    """ Renders user preferences page. """

    return render_template("user_preferences.html")


@app.route('/<user_id>/contacts')
def show_user_contacts(user_id):
    """ Displays all user contact pages. """

    return render_template("contacts.html")

@app.route('/<user_id>/add_contacts')
def add_import_contacts(user_id):
    """ Allow user to add / import contacts. """

    return render_template("add_contacts.html")


if __name__ = "__main__":
    app.debut = True
    app.jinja_env.auto_reload = app.debut

    connect_to_db(app)

    # Activates DebugToolbar
    DebugToolbarExtension

    app.run(port=5000, host='0.0.0.0')