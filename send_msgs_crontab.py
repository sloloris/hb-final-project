#!/usr/bin/python

import requests
import datetime
from model import User, Contact, Relationship, Message, ScheduledMessage, connect_to_db, db
import quickstart as gmail
from server import app

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

if __name__=="__main__":
    # cron_request = requests.get(url='http://localhost:5000/send_msgs')
    connect_to_db()
    print "Connected to DB."
    send_msgs()
    print datetime.datetime.now(), cron_request

# * * * * * /Users/isabellemiller/src/hb-final-project/.venv/bin/python /Users/isabellemiller/src/hb-final-project/send_msg_crontab.py