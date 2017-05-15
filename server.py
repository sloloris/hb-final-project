""" DESCRIPTION HERE """

from jinja2 import StrictUndefined

from flask_debugtoolbar import DebugToolbarExtension
from flask import Flask, jsonify, render_template, redirect, request, flash, session

from model import User, Contact, Relationship, Message, connect_to_db, db

import json
import quickstart as gmail 
import deets # information not to post to github
import google_oauth as oauth # relevant oauth functions and methods


app = Flask(__name__)

app.secret_key = "SOMETHINGHERE"

app.jinja_env.undefined = StrictUndefined #what does this do?


@app.route('/')
def index():
    """ Landing page. """

    oauthurl = oauth.flow.step1_get_authorize_url() # method on flow to create url

    return render_template("landing.html", oauthurl=oauthurl)

@app.route('/oauthcallback', methods=['GET'])
def oauthcallback():
    """
    Redirect URI callback for Google OAuth 2.0. Auth token passed
    a URL param called 'code'
    """
    code = request.args.get('code') # gets code from auth server
    if code:
        credentials = oauth.flow.step2_exchange(code) # method to exchange code & client secret 
        # for credentials object (authenticate client)
        print 'CREDENTIALS RETURNED:'
        print credentials.get_access_token() # Returns access token and its expiration information. If the token does not exist, get one. If the token expired, refresh it.

        # TODO: create user save access token to database

    else:
        return redirect("/")


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

@app.route('/<user_id>/send')
def send_email(user_id):
    """ Test page for interactive email sending. """



    return render_template("send_email.html")


if __name__ == "__main__":
    app.debut = True
    app.jinja_env.auto_reload = app.debut

    # connect_to_db(app)

    # Activates DebugToolbar
    DebugToolbarExtension

    app.run(port=5000, host='0.0.0.0')