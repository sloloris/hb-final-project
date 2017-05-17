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

# google contacts libraries
# import atom.data # not working for some reason, already pip installed in .env
# import gdata.data
# import gdata.contacts.client
# import gdata.contacts.data



app = Flask(__name__)

app.secret_key = "SOMETHINGHERE"

app.jinja_env.undefined = StrictUndefined #what does this do?


@app.route('/')
def index():
    """ Landing page. """

    # if user already logged in, redirect to account home
    if session.get('user_id') == True: 
        user = User.query.filter_by(user_id=int(session['user_id'])).one()
        print "USER", user

        return redirect("/account_home")
    # else get oauth url
    else:
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
            user = User.query.filter_by(email=email).one()
            session['user_id'] = str(user.user_id) 

            return redirect('/account_home')

            #return render_template("user_account.html", user_id=user.user_id, email=email, name=first_name)

        elif user[0]:
            user = User.query.filter_by(email=email).one()
            session['user_id'] = str(user.user_id) 
            session['oauth_credentials'] = credentials.get_access_token()

            # update oauth credentials in database
            user.oauth_token = session['oauth_credentials'][0]
            user.oauth_expiry = datetime.datetime.now() + datetime.timedelta(seconds=session['oauth_credentials'][1])


            db.session.commit()

            # contacts = requests.get("https://www.google.com/m8/feeds/contacts/%s/full" % (email))
            # import pdb;pdb.set_trace()
            return redirect('/account_home')
            # return render_template("user_account.html", user_id=user.user_id, email=email, name=first_name)

    else:
        flash("Something went wrong.")
        return redirect("/") 


@app.route('/about')
def about():
    """ App about page. """

    return render_template("about.html")


@app.route('/logout')
def render_login_form(): # can I do this on the front end?
    """ Ends user session (logs user out). """

    print "Logging out."
    session.clear()
    flash("You are now logged out.")

    return redirect('/')


@app.route('/account_home')
def show_user_account_home():
    """ Renders user account homepage. """

    user = User.query.filter_by(user_id=int(session['user_id'])).one()
    print user

    return render_template("user_account.html", user_id=user.user_id, name=user.first_name)
    #, user_id=user.user_id, email=email, name=first_name)


@app.route('/<user_id>/preferences', methods=["GET"])
def user_preferences(user_id):
    """ Renders user preferences page. """

    user = User.query.filter_by(user_id=int(session['user_id'])).one()

    return render_template("user_preferences.html", user_id=user.user_id, name=user.first_name)


@app.route('/<user_id>/preferences', methods=["POST"])
def update_user_preferences(user_id):
    """ Updates user preferences in database. """

    nickname = request.form.get('nickname')
    phone = request.form.get('phone')
    whatsapp = request.form.get('whatsapp')

    user = User.query.filter_by(user_id=int(session['user_id'])).one()
    # for nullable values:
    user.nickname = nickname or None # if nickname, set to nickname; else set to None
    user.phone = str(phone) or None
    if whatsapp == "yes":
        whatsapp_number = request.form.get('whatsapp_number')
        user.whatsapp = whatsapp_number

    db.session.commit()

    flash("Your preferences have been updated.")
    return render_template("user_preferences.html", user_id=user.user_id, name=user.first_name)


@app.route('/<user_id>/contacts') #add <user_id>
def show_user_contacts(user_id):
    """ Displays all user contact pages. """

    user = User.query.filter_by(user_id=int(session['user_id'])).one()
    email = str(user.email)
    print type(email), email

    # authorize client for Contacts API
    # gd_client = gdata.contacts.client.ContactsClient(source='Contact Manager 1.0')

    contacts = requests.get("https://www.google.com/m8/feeds/contacts/%s/full" % (email))
    # import pdb;pdb.set_trace();
    print contacts # response 401 unauthorized

    return render_template("contacts.html")

@app.route('/<user_id>/add_contacts')
def add_import_contacts(user_id):
    """ Allow user to add / import contacts. """

    return render_template("add_contacts.html")

@app.route('/<user_id>/send')
def send_email(user_id):
    """ Test page for interactive email sending. """



    return render_template("send_email.html")


@app.route('/<user_id>/messages')
def messages_page(user_id):

    return render_template


if __name__ == "__main__":
    app.debug = True
    app.jinja_env.auto_reload = app.debug

    connect_to_db(app)

    # Activates DebugToolbar
    DebugToolbarExtension(app)

    app.run(port=5000, host='0.0.0.0')