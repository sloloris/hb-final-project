import requests
import datetime

cron_request = requests.get(url='http://localhost:5000/send_msgs')
print datetime.datetime.now(), cron_request

# * * * * * /usr/bin/python /Users/isabellemiller/src/schedule.py > /Users/isabellemiller/src/cron.log