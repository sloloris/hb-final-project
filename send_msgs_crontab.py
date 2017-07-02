#!/usr/bin/python

import requests
import datetime

if __name__=="__main__":
    cron_request = requests.get(url='http://localhost:5000/send_msgs')
    print datetime.datetime.now(), cron_request

# * * * * * /Users/isabellemiller/src/hb-final-project/.venv/bin/python /Users/isabellemiller/src/hb-final-project/send_msg_crontab.py