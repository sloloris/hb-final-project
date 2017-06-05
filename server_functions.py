""" FUNCTIONS FOR SERVER.PY """

from jinja2 import StrictUndefined

from flask_debugtoolbar import DebugToolbarExtension
from flask import Flask, jsonify, render_template, redirect, request, flash, session

from model import User, Contact, Relationship, Message, connect_to_db, db

import json
import quickstart as gmail 
import google_oauth as oauth # relevant oauth functions and methods
import requests 
import datetime

# google contacts libraries
import atom.data
import gdata.data
import gdata.contacts.client
import gdata.contacts.data

import re # regular expressions


def get_user_info_from_google(oauth_token):
    # get user info from google
    user_info = (requests.get("https://www.googleapis.com/oauth2/v1/userinfo?access_token=%s" % oauth_token)).json()
    first_name = user_info['given_name']
    last_name = user_info['family_name']
    email = user_info['email']

    return [first_name, last_name, email]

# FOR TESTS: CREATE FAKE CREDENTIALS
def create_update_user_in_db(credentials, email, first_name, last_name, oauth_token, oauth_expiry, refresh_token):
    user = User.query.filter_by(email=email).all()
    if user == []:
        # instantiate new user object in database
        new_user = User(first_name=first_name, last_name=last_name, email=email, oauth_token=oauth_token, oauth_expiry=oauth_expiry, refresh_token=refresh_token) #sqlalchemy instantiation of user

        db.session.add(new_user)
        db.session.commit()

        # start a flask session for user
        user = User.query.filter_by(email=email).one()
        session['user_id'] = str(user.user_id) 

        print 'New user with id %s added to database.' % (session['user_id'])

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
        print 'Oauth credentials updated for user %s in database.' % (session['user_id'])
        

# INTEGRATION TEST ONLY
def get_google_contacts(credentials):
    """ Gets user's Google contacts from Contacts API. """

    # authorize client contacts
    auth2token = gdata.gauth.OAuth2Token(client_id=credentials.client_id, client_secret=credentials.client_secret, scope='https://www.google.com/m8/feeds/contacts/default/full', access_token=credentials.access_token, refresh_token=credentials.refresh_token, user_agent='Contact Manager 1.0')
    client = gdata.contacts.client.ContactsClient()
    auth2token.authorize(client)
    updated_min = '2014-01-01' # starting date after which to retrieve contacts
    query = gdata.contacts.client.ContactsQuery()
    query.max_results = 9999
    query.updated_min = updated_min
    feed = client.GetContacts(q=query)

    if feed:
        print "CONTACT FEED RETURNED"
    
    contact_file = open('contact_output.txt', 'w') # 'w' for write capabilities
    contact_file.write(str(feed))
    contact_file.close()
    
    print "CONTACTS PIPED TO CONTACT_OUTPUT.TXT"


def clean_google_contact_data(user_email):
    """ Takes text file of data returned from Google Contacts API and reformats into list of dictionaries containing first_name, last_name, and email. """

    contact_file = open('contact_output.txt')
    contact_list = []
    for line in contact_file:
        first_name = re.findall(r'(?<=<ns1:givenName>)(.*)(?=</ns1:givenName>)', line)
        last_name = re.findall(r'(?<=<ns1:familyName>)(.*)(?=</ns1:familyName>)', line)
        email = re.findall(r'[\w\.-]+@[\w\.-]+', line)

        contact = {}
        if email and len(email[0]) < 50:
            if first_name and len(first_name[0]) < 20:
                contact['first_name'] = first_name[0]
            else:
                contact['first_name'] = None
            if last_name and len(last_name[0]) < 30:
                contact['last_name'] = last_name[0]
            else:
                contact['last_name'] = None
            contact['email'] = email[0]

        if contact:
            contact_list.append(contact)

    contact_file.close()
    print "CONTACT LIST CREATED"
    return contact_list
  

def save_user_contacts_to_db(user_id, contact_list):
    """ Saves all user contacts from Google Contacts API into contacts table. """

    for contact in contact_list:
        # raise Exception
        contact_query = Contact.query.filter_by(email=contact['email']).all()
        if not contact_query:
            new_contact = Contact(user_id=user_id, first_name=contact['first_name'], last_name=contact['last_name'], email=contact['email'])
            db.session.add(new_contact)

    # figure out a better way to do this later
    Contact.query.filter_by(first_name=None).delete()
    Contact.query.filter_by(last_name=None).delete()

    db.session.commit()

    print "%d contacts added to database for user %s." % (len(contact_list), user_id)



