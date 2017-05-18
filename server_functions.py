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

import re # regular expressions
import xml.etree.ElementTree as ET


def get_google_contacts(credentials):
    """ Gets user's Google contacts from Contacts API. """

    # authorize client contacts
    auth2token = gdata.gauth.OAuth2Token(client_id=credentials.client_id, client_secret=credentials.client_secret, scope='https://www.google.com/m8/feeds/contacts/default/property-KEY', access_token=credentials.access_token, refresh_token=credentials.refresh_token, user_agent='Contact Manager 1.0')
    client = gdata.contacts.client.ContactsClient()
    auth2token.authorize(client)
    updated_min = '2014-01-01' # date from which to retrieve contacts
    query = gdata.contacts.client.ContactsQuery()
    query.max_results = 100
    query.updated_min = updated_min
    feed = client.GetContacts(q=query) # TODO: figure out how to refactor this into /contacts and parse it

    if feed:
        print "CONTACT FEED RETURNED"
        print feed
    
    # for testing purposes
    contact_file = open('contact_output.txt', 'w') # 'w' for write capabilities
    contact_file.write(str(feed))
    contact_file.close()
    

    print "CONTACTS PIPED TO CONTACT_OUTPUT.TXT"

    contact_file = open('contact_output.txt')
    contact_list = []
    for line in contact_file:
        first_name = re.findall(r'(?<=<ns1:givenName>)(.*)(?=</ns1:givenName>)', line)
        last_name = re.findall(r'(?<=<ns1:familyName)(.*)(?=</ns1:familyName>)', line)
        email = re.findall(r'[\w\.-]+@[\w\.-]+', line)
        contact = [first_name, last_name, email]
        for item in contact:
            if item == []:
                item = None
            else: item = item[0]
        if not contact == [[], [], []]:
            contact_list.append(contact)

    print contact_list

    contact_file.close()

  

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
        
