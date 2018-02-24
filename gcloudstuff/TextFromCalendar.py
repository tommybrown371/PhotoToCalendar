import io
import os
import requests
from google.cloud import vision
from google.cloud.vision import types
import json

vision_client = vision.ImageAnnotatorClient()
file_name = os.path.join(
    os.path.dirname(__file__),
    '/Users/tommybrown371/Desktop/gcloudstuff/calendar_example_2.png')

with io.open(file_name, 'rb') as image_file:
    content = image_file.read()

image = types.Image(content=content)
response = vision_client.text_detection(image=image)
labels = response.text_annotations 

for label in labels:
    print(label.description)

