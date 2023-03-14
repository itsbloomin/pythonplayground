# Goal: Setup and use Yahoo Fantasy Sports API
    # https://developer.yahoo.com/oauth2/guide/
    # https://developer.yahoo.com/fantasysports/guide/
    # create API Key: https://developer.yahoo.com/apps/create/
    # OAuth Required

# My App and Key Info :: Remove from Public
    # https://developer.yahoo.com/apps/kUGjh6hs/
    # App ID: kUGjh6hs
    # Client ID (Consumer Key): dj0yJmk9R29Jek9GcjBQMEdzJmQ9WVdrOWExVkhhbWcyYUhNbWNHbzlNQT09JnM9Y29uc3VtZXJzZWNyZXQmc3Y9MCZ4PTBk
    # Client Secret (Consumer Secret): 5eb1f31e434264055de63041fb4a6c42e3d8039a
    # redirect URI: https://example.com/redirect

# example: https://joinative.com/yahoo-gemini-api-oauth-authentication-python
# https://pypi.org/project/yahoo-oauth/
# https://www.youtube.com/watch?v=C0WjwBtwS9Y

from requests import get, post
import json
import webbrowser
import base64

client_id = ""
client_secret = "jhjh"
base_url = "https://api.login.yahoo.com/"

# REDIRECT_URI = "https://example.com/redirect"

code_url = f'oauth2/request_auth?client_id={client_id}&redirect_uri=oob&response_type=code&language=en-us'
# webbrowser.open(base_url + code_url)
print("URL: " + base_url + code_url)
code = 'urxdy73'
print("code: " + code)

encoded = base64.b64encode((client_id + ':' + client_secret).encode("utf-8"))
headers = {
    'Authorization': f'Basic {encoded.decode("utf-8")}',
    'Content-Type': 'application/x-www-form-urlencoded'
}
data = {
    'grant_type': 'authorization_code',
    'redirect_uri': 'oob',
    'code': code
}
response = post(base_url + 'oauth2/get_token', headers=headers, data=data)
print(response.ok)
print(response.json())

access_token = response.json()['access_token']
refresh_token = response.json()['refresh_token']
print("Access Token: " + access_token)
print("Refresh Token: " + refresh_token)





