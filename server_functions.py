""" FUNCTIONS FOR SERVER.PY """

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
import atom.data
import gdata.data
import gdata.contacts.client
import gdata.contacts.data


def get_google_contacts(credentials):
    """ Gets user's Google contacts from Contacts API. """

    # authorize client contacts
    auth2token = gdata.gauth.OAuth2Token(client_id=credentials.client_id, client_secret=credentials.client_secret, scope='https://www.google.com/m8/feeds/contacts/default/full', access_token=credentials.access_token, refresh_token=credentials.refresh_token, user_agent='Contact Manager 1.0')
    client = gdata.contacts.client.ContactsClient()
    auth2token.authorize(client)
    query = gdata.contacts.client.ContactsQuery()
    query.max_results = 100
    feed = client.GetContacts(q=query) # TODO: figure out how to refactor this into /contacts and parse it
    
    # for testing purposes
    contact_file = open('contact_output.txt', 'w') # 'w' for write capabilities
    contact_file.write(str(feed))
    contact_file.close()

    print "CONTACTS PIPED TO CONTACT_OUTPUT.TXT"
    if feed:
        print "CONTACT FEED RETURNED"
        for i,entry in enumerate(feed.entry):
            # if entry.email[0]:
            #     print entry.email.json() or entry.phone or None
            # if not entry.name is None:
            #       family_name = entry.name.family_name is None and " " or entry.name.family_name.text
            #       full_name = entry.name.full_name is None and " " or entry.name.full_name.text
            #       given_name = entry.name.given_name is None and " " or entry.name.given_name.text
            #       print '\n%s %s: %s - %s' % (i+1, full_name, given_name, family_name)
            #       print "tada!"
            if not entry.name is None:
                print '\n%s %s' % (i+1, entry.name.full_name.text)
            if entry.content:
                print '    %s' % (entry.content.text)
            # Display the primary email address for the contact.
            if not entry.email[0] is None:
                for email in entry.email:
                    if email.primary and email.primary == 'true':
                        print '    %s' % (email.address)


def get_user_info_from_google(oauth_token):
    # get user info from google
    user_info = (requests.get("https://www.googleapis.com/oauth2/v1/userinfo?access_token=%s" % oauth_token)).json()
    first_name = user_info['given_name']
    last_name = user_info['family_name']
    email = user_info['email']

    return [first_name, last_name, email]

def create_update_user_in_db(credentials, email):
    user = User.query.filter_by(email=email).all()
    if user == []:
        # instantiate new user object in database
        new_user = User(first_name=first_name, last_name=last_name, email=email, oauth_token=oauth_token,oauth_expiry=oauth_expiry) #sqlalchemy instantiation of user

        db.session.add(new_user)
        db.session.commit()

        # start a flask session for user
        user = User.query.filter_by(email=email).one()
        session['user_id'] = str(user.user_id) 

        return redirect('/account_home')

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
        
