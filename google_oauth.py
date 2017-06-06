import logging
from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
from apiclient.discovery import build
from oauth2client.client import OAuth2WebServerFlow
import os

CLIENTSECRETS_LOCATION = '<CLIENT_SECRETS.JSON>'
REDIRECT_URI = ["http://localhost"] # '<YOUR_REGISTERED_REDIRECT_URI>'
SCOPES = [
    'https://www.googleapis.com/auth/gmail.compose', # create, read, update & delete drafts. send messages & drafts
    # 'https://www.googleapis.com/auth/gmail.labels', # create, read, update & delete labels
    'https://www.googleapis.com/auth/gmail.modify', # all read/write permissions
    'https://www.google.com/m8/feeds/', # access to user contacts
    'https://www.googleapis.com/auth/contacts.readonly',
    'https://www.googleapis.com/auth/userinfo.profile',
    'https://www.googleapis.com/auth/userinfo.email'
]

# creates Oauth2 object with method to create auth URL
# need to set access mode to offline
flow = OAuth2WebServerFlow(client_id=os.environ['client_id'],
                           client_secret=os.environ['client_secret'],
                           scope=SCOPES,
                           redirect_uri='http://localhost:5000/oauthcallback',
                           prompt='consent')
flow.params['access_type'] = 'offline'
