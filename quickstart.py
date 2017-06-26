import httplib2
import os
import oauth2client
from oauth2client import client, tools
import base64
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from apiclient import errors, discovery
from email import encoders

from oauth2client.client import GoogleCredentials
from oauth2client import GOOGLE_TOKEN_URI

from model import User, Contact, Relationship, Message, connect_to_db, db


SCOPES = ['https://www.googleapis.com/auth/gmail.send',
        'https://www.googleapis.com/auth/gmail.compose', # create, read, update & delete drafts. send messages & drafts
        'https://www.googleapis.com/auth/gmail.labels', # create, read, update & delete labels
        'https://www.googleapis.com/auth/gmail.modify']
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Gmail API Python Send Email'

# def get_credentials():
#     home_dir = os.path.expanduser('~')
#     credential_dir = os.path.join(home_dir, '.credentials')
#     if not os.path.exists(credential_dir):
#         os.makedirs(credential_dir)
#     credential_path = os.path.join(credential_dir, 'gmail-python-email-send.json')
#     store = oauth2client.file.Storage(credential_path)
#     credentials = store.get()
#     print credentials
#     if not credentials or credentials.invalid:
#         flow = client.flow_from_clientsecrets('client_secret.json', SCOPES)
#         flow.user_agent = 'Contact Manager 1.0'
#         credentials = tools.run_flow(flow, store)
#         print('Storing credentials to ' + credential_path)
#     return credentials

def get_credentials(sender_email):
    user = User.query.filter_by(email=sender_email).one()
    access_token = user.oauth_token
    token_expiry = user.oauth_expiry
    token_uri = GOOGLE_TOKEN_URI # os.environ['token_uri']
    user_agent = 'Python client library'
    revoke_uri = None
    client_id = os.environ['client_id']
    client_secret = os.environ['client_secret']
    refresh_token = user.refresh_token

    credentials = GoogleCredentials( 
        access_token, 
        client_id,
        client_secret, 
        refresh_token, 
        token_expiry,
        token_uri, 
        user_agent,
        revoke_uri=revoke_uri
    )

    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets('client_secret.json', SCOPES)
        flow.user_agent = 'Contact Manager 1.0'
        credentials = tools.run_flow(flow)
        user.oauth_token = credentials.refresh_token
        user.oauth_expiry = credentials.token_expiry
        db.sessions.commit()
        print('Storing credentials to database')
    return credentials


def SendMessage(sender, to, subject, msgHtml, msgPlain):
    credentials = get_credentials(sender)
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('gmail', 'v1', http=http)
    message1 = CreateMessage(sender, to, subject, msgHtml, msgPlain)
    SendMessageInternal(service, "me", message1)

def SendMessageInternal(service, user_id, message):
    try:
        message = (service.users().messages().send(userId=user_id, body=message).execute())
        print('Message Id: %s' % message['id'])
        return message
    except errors.HttpError as error:
        print('An error occurred: %s' % error)

def CreateMessage(sender, to, subject, msgHtml, msgPlain):
    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = to
    msg.attach(MIMEText(msgPlain, 'plain'))
    msg.attach(MIMEText(msgHtml, 'html'))
    print msg
    raw = base64.urlsafe_b64encode(msg.as_string())
    # raw = raw.decode()
    body = {'raw': raw}
    return body

def main():
    to = os.environ['isa_email']
    sender = os.environ['isa_email']
    subject = "test test"
    msgHtml = "Hi<br/>Html Email"
    msgPlain = "Hi\nPlain Email"
    SendMessage(sender, to, subject, msgHtml, msgPlain)

if __name__ == '__main__':
    main()