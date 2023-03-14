# https://github.com/d4vidsha/implementing-oauth-2.0-with-python/blob/main/example-oauth-2.0-with-client-credentials.py
import requests
from requests import request
import json
from datetime import datetime
import webbrowser
import base64

# constants
CLIENT_ID = ""
CLIENT_SECRET = ""
#test
# obtain access token
base_url = "https://api.login.yahoo.com"
code_url = f'oauth2/request_auth?client_id={CLIENT_ID}&redirect_uri=oob&response_type=code&language=en-us'
# print(base_url + code_url) # https://api.login.yahoo.comoauth2/request_auth?client_id=dj0yJmk9R29Jek9GcjBQMEdzJmQ9WVdrOWExVkhhbWcyYUhNbWNHbzlNQT09JnM9Y29uc3VtZXJzZWNyZXQmc3Y9MCZ4PTBk&redirect_uri=oob&response_type=code&language=en-us

encoded = base64.b64encode((CLIENT_ID + ':' + CLIENT_SECRET).encode("utf-8"))
headers = {
    'Authorization': f'Basic {encoded.decode("utf-8")}',
    'Content-Type': 'application/x-www-form-urlencoded'
}
data = {
    'grant_type': 'authorization_code',
    'redirect_uri': 'oob',
    'code': 'code'
}
response = requests.post(base_url + 'oauth2/get_token', headers=headers, data=data)

# data = {
#    "grant_type": "client_credentials",
#    "scope": "oapi"
# }


# response = request("POST", url, auth=(CLIENT_ID, CLIENT_SECRET), data=data)
# print(json.dumps(response.json(), indent=4))
# access_token = response.json()["access_token"]
# token_type = response.json()["token_type"]

# make the request
# now = datetime.now().isoformat()
# url = f"https://oapi.lup.com.au/api/v1/events/{EVENT_ID}/visitors"
#headers = {
#    "Authorization": token_type + SPACE + access_token,
#    "Content-Type": "application/json"
# }

# response = request("GET", url, headers=headers)
# print(response.text)