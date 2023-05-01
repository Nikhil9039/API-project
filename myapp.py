import requests
import json
from datetime import datetime

URL="http://127.0.0.1:8000/api_app/"

def get_data(id=None):
    data={}
    if id is not None:
        data={'id':id}
    json_data=json.dumps(data)
    r=requests.get(url=URL, data=json_data)
    data=r.json()
    print(data)
# get_data()

# Function for inserting/creating data
import base64
def post_data():

    
    data={
        'type':'event',
        'name':'Meeting',
        'tagline':'Introducing our latest innovation',
        'schedule': datetime(2023, 5, 10, 12, 30).strftime("%Y-%m-%d %H:%M:%S"),
        'description':'A product launch is an event that introduces a new product to the market. The tagline "Introducing our latest innovation" highlights the newness and innovation of the product being launched and generates excitement and anticipation among attendees.',
        'files': None, 
        'moderator':'jack',
        'category':'launching',
        'sub_category':'product launching',
        'rigor_rank':9,
        'attendees':'raj, rajesh, jack'
    }
    json_data=json.dumps(data)
    r=requests.post(url=URL, data=json_data)
    data=r.json()
    print(data)
post_data()

# Function for updating data
def update_data():
    data={
        'id':3,
        'name':'MyProduct launch',
        'tagline':'We are Introducing our latest innovation',
        'schedule': datetime(2023, 5, 10, 12, 30).strftime("%Y-%m-%d %H:%M:%S"),
        'description':'A product launch is an event that introduces a new product to the market. The tagline "Introducing our latest innovation" highlights the newness and innovation of the product being launched and generates excitement and anticipation among attendees.',
        'files': None, 
        'moderator':'jackie',
        'category':'Mylaunching',
        'sub_category':'Myproduct launching',
        'rigor_rank':6
    }
    json_data=json.dumps(data)
    r=requests.put(url=URL, data=json_data)
    data=r.json()
    print(data)
# update_data()

#Function for deleting a data
def delete_data():
    data={'id':3}
    json_data=json.dumps(data)
    r=requests.delete(url=URL, data=json_data)
    data=r.json()
    print(data)
# delete_data()

