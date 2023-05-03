import logging
import os
import datetime
import urllib.request
import json


date = str(datetime.date.today())
l = logging.getLogger()
l.setLevel(logging.INFO)

def lmdr(event, context):
    
    me = event['events'][0]

    url = 'https://api.line.me/v2/bot/message/reply'

    retu = create(me['message']['text'])


    head = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + os.environ['ACCESSTOKEN']
    }

    data = {
        'replyToken': me['replyToken'],
        'messages': [
            {
                "type": "text",
                "text": retu,
            }
        ]
    }
    y = urllib.request.Request(url=url, data=json.dumps(data).encode('utf-8'), method='POST', head=head)
    
    with urllib.request.urlopen(y) as res:
        
        l.info(res.read().decode("utf-8"))

def create(text):
    if 'today?' == text:
        return date
    else:
        return text