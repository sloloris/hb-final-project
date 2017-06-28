import requests
import datetime
# import quickstart as gmail

# messages = Message.query.filter((Message.created_by==user.user_id) | (Message.created_by==1)).all()
# random_int = random.randint(0, len(messages) - 1)

# cron job + query database for user email
# gmail.SendMessage(sender, to, subject, msgHtml, msgPlain)
# gmail.SendMessage(user.email, contact.email, 'Hey', msg_text, msg_text)
# print 'Message sent'

cron_request = requests.get(url='http://localhost:5000/send_msgs')
print datetime.datetime.now(), cron_request

# * * * * * /usr/bin/python /Users/isabellemiller/src/schedule.py > /Users/isabellemiller/src/cron.log