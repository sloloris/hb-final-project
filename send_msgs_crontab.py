import requests
import datetime
# from server import app
# from model import Message, User, ScheduledMessage, Contact, connect_to_db, db
# import quickstart as gmail

# # connect to database
# connect_to_db(app)
# print "Connected to DB."

# current_time = datetime.datetime.now()
# # query database for all scheduled messages that are due
# scheduled = ScheduledMessage.query.filter(ScheduledMessage.send_date<=current_time).all()
# scheduled = ScheduledMessage.query.filter( (ScheduledMessage.send_date<=datetime.datetime.now() & (ScheduledMessage.sent==false) ).all()


# # query database for all message templates belonging to user
# messages = Message.query.filter((Message.created_by==user.user_id) | (Message.created_by==1)).all()
# random_int = random.randint(0, len(messages) - 1)

# user = 
# gmail.SendMessage(sender, to, subject, msgHtml, msgPlain)
# gmail.SendMessage(user.email, contact.email, 'Hey', msg_text, msg_text)
# print 'Message sent'
if __name__=="__main__":
    cron_request = requests.get(url='http://localhost:5000/send_msgs')
    print datetime.datetime.now(), cron_request

# * * * * * /usr/bin/python /Users/isabellemiller/src/schedule.py > /Users/isabellemiller/src/cron.log