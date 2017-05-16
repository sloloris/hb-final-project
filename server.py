""" DESCRIPTION HERE """

from jinja2 import StrictUndefined

from flask_debugtoolbar import DebugToolbarExtension
from flask import Flask, jsonify, render_template, redirect, request, flash, session

from model import User, Contact, Relationship, Message, connect_to_db, db

import json
import quickstart as gmail 
import deets # information not to post to github
import google_oauth as oauth # relevant oauth functions and methods
import requests 
import datetime


app = Flask(__name__)

app.secret_key = "SOMETHINGHERE"

app.jinja_env.undefined = StrictUndefined #what does this do?


@app.route('/')
def index():
    """ Landing page. """

    oauthurl = oauth.flow.step1_get_authorize_url() # method on flow to create url

    return render_template("landing.html", oauthurl=oauthurl) # pass url to landing page

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

        # add credentials to session
        session['oauth_credentials'] = credentials.get_access_token()

        oauth_credentials = credentials.get_access_token()
        oauth_token = oauth_credentials[0]
        oauth_expiry = datetime.datetime.now() + datetime.timedelta(seconds=oauth_credentials[1])

        # get user info from google
        user_info = (requests.get("https://www.googleapis.com/oauth2/v1/userinfo?access_token=%s" % oauth_token)).json()
        first_name = user_info['given_name']
        last_name = user_info['family_name']
        email = user_info['email']

        user = User.query.filter_by(email=email).all()
        if user == []:
            new_user = User(first_name=first_name, last_name=last_name, email=email, oauth_token=oauth_token,oauth_expiry=oauth_expiry) #sqlalchemy instantiation of user

            db.session.add(new_user)
            db.session.commit()
            # start a flask session for user
            session['user_id'] = str(users.user_id)
        else:
            flash("User already exists. Please log in.")

        return redirect('/')

    else:
        flash("Something went wrong.")
        return redirect("/") 


@app.route('/about')
def about():
    """ App about page. """

    return render_template("about.html")


# @app.route('/register', methods=["GET"])
# def register_form():
#     """ Renders user registration form. """

#     return render_template('registration.html')

# @app.route('/register', methods=["POST"])
# def register():
#     """ User account registration form. """

#     first_name = request.form.get("first_name")
#     last_name = request.form.get("last_name")
#     nickname = request.form.get("nickname")
#     # email = request.get("https://www.googleapis.com/oauth2/v2/userinfo")
#     phone = request.form.get("phone")
#     whatsapp = request.form.get("whatsapp")

#     oauth_credentials = session['oauth_credentials']
#     oauth_token = oauth_credentials[0]
#     oauth_expiry = datetime.datetime.now() + datetime.timedelta(seconds=oauth_credentials[1])
#     # not an accurate date - how to fix?

#     user_info = (requests.get("https://www.googleapis.com/oauth2/v1/userinfo?access_token=%s" % oauth_token)).json()

#     user = User.query.filter_by(email=email).all()
#     if user == []:
#         new_user = User(first_name=first_name, last_name=last_name, email=email, oauth_token=oauth_token, oauth_expiry=oauth_expiry) #sqlalchemy instantiation of user
#         # for nullable values:
#         new_user.nickname = nickname or None # if nickname, set to nickname; else set to None
#         new_user.phone = phone or None
#         new_user.whatsapp = whatsapp or None

#     db.session.add(new_user)
#     db.session.commit()

#     print "oauth token = ", oauth_token
#     print "oauth expiry = ", oauth_expiry
#     print "user info = ", user_info
#     return render_template('registration.html')


# @app.route('/login', methods=["GET"])
# def render_login_form(): # can I do this on the front end?
#     """ Renders login form. """

#     return render_template("login.html")


# @app.route('/login', methods=["POST"])
# def login_user():
#     """ Initiates new Flask session for user. """

#     return redirect("/login")


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
    app.debug = True
    app.jinja_env.auto_reload = app.debug

    connect_to_db(app)

    # Activates DebugToolbar
    DebugToolbarExtension(app)

    app.run(port=5000, host='0.0.0.0')