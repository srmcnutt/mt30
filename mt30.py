
import requests
import json 
import os
from random import randrange
from flask import Flask, request, jsonify

SEARCH = 'stimpy button'
GIPHY_KEY = os.environ.get('GIPHY_KEY')
API_KEY = os.environ.get('API_KEY')
LIMIT = 25
WEBEX_URL = 'https://webexapis.com/v1/messages'
WEBEX_KEY = os.environ.get('WEBEX_KEY')
WEBEX_ROOM = os.environ.get('WEBEX_ROOM')

from requests import Session
class NoRebuildAuthSession(Session):
    def rebuild_auth(self, prepared_request, response):
      '''
      No code here means requests will always preserve the Authorization header when redirected.
      Be careful not to leak your credentials to untrusted hosts!
      '''
# session = NoRebuildAuthSession()
# response = session.get('https://api.meraki.com/api/v1/organizations/', headers={'Authorization': f'Bearer {API_KEY}'})
# body = response.json()
# print(json.dumps(body, indent = 4))

def get_giphy_url(search):
    r = 0
    r = int(randrange(0, 26))
    url = f'https://api.giphy.com/v1/gifs/search?api_key={GIPHY_KEY}&q={search}&limit={LIMIT}&offset=0&rating=g&lang=en'
    response = requests.get(url)
    body = response.json()
    result =  body['data'][r]['images']['original']['url']
    print(result)
    return result

def post_gif_to_webex(gif):
 

    url=WEBEX_URL
    
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + WEBEX_KEY
    }
    payload = {
    "roomId" : f"{WEBEX_ROOM}",
    "html" : f"<p>Here's a ren and stimpy image of (probably) a shiny red button!</p></br> {gif}" 
  }


    response = requests.request("POST", url, headers=headers, json=payload)
    print(payload)
    print(response.text)
    return

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def hello():
    body = request.json
    # print(json.dumps(body, indent = 4))
    # print(body["alertData"]["message"])
    gif = get_giphy_url(SEARCH)
    post_gif_to_webex(gif)
    
    return "Hello, World!"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5050)