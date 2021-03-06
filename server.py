""" Python server for FriendKeeper app. """

from jinja2 import StrictUndefined

from flask_debugtoolbar import DebugToolbarExtension 
from flask import Flask, jsonify, render_template, redirect, request, flash, session

from model import User, Contact, Relationship, Message, ScheduledMessage, connect_to_db, db
from server_functions import get_google_contacts, get_user_info_from_google, create_update_user_in_db, clean_google_contact_data, save_user_contacts_to_db

import os
import re # regex

import json
import quickstart as gmail # relevant gmail functions
import google_oauth as oauth # relevant oauth functions and methods
import requests
import datetime
from dateutil import parser # for converting to datetime objects

import time
import random

# google contacts libraries
import atom.data
import gdata.data
import gdata.contacts.client
import gdata.contacts.data

app = Flask(__name__)

app.secret_key = "SOMETHINGHERE"

app.jinja_env.undefined = StrictUndefined # disallows all operations beside testing for undefined objects


@app.route('/')
def index():
    """ Landing page. """

    # if user already logged in, redirect to account home
    if 'user_id' in session:
        user = User.query.filter_by(user_id=int(session['user_id'])).one()
        print "USER", user, "logged in."

        return redirect("/account_home")

    # else get oauth url
    else:
        oauth.flow.params['access_type'] = 'offline'
        oauthurl = oauth.flow.step1_get_authorize_url() # method on flow to create url
   
        return render_template("landing.html", oauthurl=oauthurl) # pass url to landing page


@app.route('/oauthcallback', methods=['GET'])
def oauthcallback():
    """
    Redirect URI callback for Google OAuth 2.0. Auth token passed
    a URL param called 'code'.

    See server_functions.py for full functions.
    """
    code = request.args.get('code') # gets code from auth server
    if code:
        credentials = oauth.flow.step2_exchange(code) # method to exchange code & client secret 
        # for credentials object (authenticate client)
        print 'CREDENTIALS RETURNED:'
        print credentials.get_access_token() # Returns access token and its expiration information. If the token does not exist, get one. If the token expired, refresh it.

        # add credentials to session
        oauth_credentials = credentials.get_access_token()
        oauth_token = oauth_credentials[0]
        oauth_expiry = datetime.datetime.now() + datetime.timedelta(seconds=oauth_credentials[1])
        print credentials
        refresh_token = credentials.refresh_token
        session['oauth_token'] = oauth_token
        session['oauth_expiry'] = oauth_expiry

        # gets user info from google
        first_name, last_name, email = get_user_info_from_google(oauth_token)

        # creates or updates user in the contacts database & redirects to account page
        create_update_user_in_db(credentials, email, first_name, last_name, oauth_token, oauth_expiry, refresh_token)

        # issue get request to Google Contacts API for user contacts and pipe data into contact_output.txt
        get_google_contacts(credentials) 

        # clean data out of file and return list of contact dictionaries
        contact_list = clean_google_contact_data(email) 

        save_user_contacts_to_db(int(session['user_id']), contact_list)

        return redirect('/account_home')

    else:
        flash("Something went wrong.")
        return redirect("/")


@app.route('/about')
def about():
    """ App about page. """

    oauth.flow.params['access_type'] = 'offline'
    oauthurl = oauth.flow.step1_get_authorize_url()

    return render_template("about.html", oauthurl=oauthurl)


@app.route('/logout')
def logout_user(): 
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

    return render_template("base.html")
    # return render_template("user_account.html", user_id=user.user_id, name=user.first_name)
    #, user_id=user.user_id, email=email, name=first_name)


@app.route('/user/<user_id>/contacts', methods=["GET"]) #add <user_id>
def show_user_contacts(user_id):
    """ Sends json of user contacts to client. """

    user_contacts = Contact.query.filter_by(user_id=user_id).all()

    contacts = []
    for contact in user_contacts:
        contacts.append( { 'contact_id': contact.contact_id,
                            'first_name': contact.first_name,
                            'last_name': contact.last_name,
                            'email': contact.email } )

    return jsonify(contacts)


@app.route('/user/<user_id>/messages', methods=["GET"])
def messages_page(user_id):
    """ Sends json of user messages to client. """

    default_msgs = Message.query.filter_by(created_by=1).all()
    user_msgs = Message.query.filter_by(created_by=user_id).all()

    messages = []
    for msg in default_msgs:
        messages.append( { 'msg_id': msg.msg_id,
                            'created_by': msg.created_by,
                            'msg_text': msg.msg_text } )

    if user_msgs:
        for msg in user_msgs:
            if msg.created_by != 1:
                messages.append( { 'msg_id': msg.msg_id,
                                    'created_by': msg.created_by,
                                    'msg_text': msg.msg_text } )

    return jsonify(messages)


@app.route('/user/<user_id>/messages', methods=["POST"])
def add_new_message(user_id):
    """ Allows users to add new messages to database. """

    user_id = request.form.get('userId')
    msg_text = request.form.get('msgText')

    new_msg = Message(created_by=user_id, msg_text=msg_text)
    db.session.add(new_msg)
    db.session.commit()

    response = {'user_id': user_id,
                'msg_text': msg_text}

    print 'user_id:', user_id, 'msg_text:', msg_text
    return jsonify(response)


@app.route('/set_period', methods=["POST"])
def set_period():
    """ Set period on a contact in database according to user input on Contacts View. """

    contact_id = request.form.get('contact_id')
    period = request.form.get('value')

    contact = Contact.query.filter_by(contact_id=contact_id).first()
    contact.contact_period = int(period)
    db.session.commit()

    return 'something returned'


@app.route('/schedule', methods=["POST"])
def create_new_schedule():
    """ Save user-scheduled message to database. """

    # collect all relevant information from form
    user_id = int(session['user_id'])
    user = User.query.filter_by(user_id=int(session['user_id'])).one()
    contact_form_value = request.form.get('contact_id')
    start_date_unicode = request.form.get('start_date')
    period = int(request.form.get('period'))

    # extracts email from contact_form_value string using re library
    contact_email = contact_form_value.partition('<')[-1].rpartition('>')[0]

    # pull contact from database
    contact = Contact.query.filter_by(email=contact_email).one()
    contact_id = contact.contact_id

    # turns start_date into datetime object using dateutil library
    start_date = parser.parse(start_date_unicode)

    # calculates send_date from start_date and period
    send_date = start_date + datetime.timedelta(days=period)

    # write scheduled message to database
    new_scheduled_msg = ScheduledMessage(user_id=user_id, 
                                        contact_id=contact_id,
                                        send_date=send_date,
                                        sent=False)

    # set new period on contact in database
    contact.contact_period = period

    db.session.add(new_scheduled_msg)
    db.session.commit()

    print 'user_id:', user_id
    print 'contact_form_value:', contact_form_value
    print 'start_date:', start_date, 'type:', type(start_date)
    print 'contact_email:', contact_email
    print 'contact:', contact
    print 'contact_id:', contact.contact_id
    print 'period:', period
    print 'send_date:', send_date
    return jsonify({})

@app.route('/send_msgs', methods=["GET"])
def send_msgs():
    """ Cron job to check for and send overdue messages. """

    scheduled = ScheduledMessage.query.filter( (ScheduledMessage.send_date<=datetime.datetime.now()) & (ScheduledMessage.sent=='f') ).all()
    print "scheduled msgs = ", scheduled

    for msg in scheduled:
        user = User.query.filter_by(user_id=msg.user_id).one()
        contact = Contact.query.filter_by(contact_id=msg.contact_id).one()
        messages = Message.query.filter((Message.created_by==user.user_id) | (Message.created_by==1)).all()
        random_int = random.randint(0, len(messages) - 1)
        msg_text = messages[random_int].msg_text
        gmail.SendMessage(user.email, contact.email, 'Hey', msg_text, msg_text)
        msg.sent = True
        # schedule next message
        next_msg = ScheduledMessage(user_id=user.user_id, 
                                    contact_id=contact.contact_id,
                                    send_date=msg.send_date + datetime.timedelta(days=contact.contact_period),
                                    sent=False)
        db.session.add(next_msg)
        db.session.commit()
        print "sent message"

    return "All scheduled messages sent."


if __name__ == "__main__":
    app.debug = False
    app.jinja_env.auto_reload = app.debug


    connect_to_db(app)

    # Activates DebugToolbar
    # DebugToolbarExtension(app)

    app.run(port=5000, host='0.0.0.0', threaded=True)