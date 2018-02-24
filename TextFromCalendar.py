import io
import os
import requests
from google.cloud import vision
from google.cloud.vision import types
import json
import time
from datetime import date, datetime
from __future__ import print_function
import httplib2

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/calendar-python-quickstart.json
SCOPES = 'https://www.googleapis.com/auth/calendar.readonly'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Google Calendar API Python Quickstart'

print "checkpoint1"
vision_client = vision.ImageAnnotatorClient()
file_name = os.path.join(
    os.path.dirname(__file__),
    '/Users/tommybrown371/Desktop/gcloudstuff/time_example_1.png')
print "checkpoint2"

with io.open(file_name, 'rb') as image_file:
    content = image_file.read()

print "checkpoint3"

image = types.Image(content=content)
print "checkpoint4"

response = vision_client.text_detection(image=image)
print "checkpoint5"

labels = response.text_annotations 
print "checkpoint6"

labels = labels[0].description.split("\n")

for label in labels:
	print label

time = labels[0]
time = time.split(" ")
summary = labels[1]
#print(time)
#intTime = int(time[0:1])
miliSec = ":00%s"
#if time.lower.endswith("pm"):
#	intTime = intTime + 12
dtime = date.today()
totalTime = str(dtime) + "T" + time[0] + miliSec
print(totalTime)

#print(dtime.isoformat())
#dtime = time.isoformat()

#EVENT = {
#	'summary': summary,
#	'start': {'dateTime': totalTime},
#	'end': {'dateTime': totalTime},
#}

#service = build('calendar', 'v3', http=creds.authorize(Http()))
#event = service.events().insert(calendarId='primary', body=event).execute()


#print(labels)
# i = 0
# for label in labels:
#     print(label.description)
#     print i
#     i = i + 1

#lst = labels.splitLines()
#for line in lst:
#	if (line.lower.endswith(am) or line.lower.endswith(pm)):
#		currentTime = line
#		timeSet = true	

