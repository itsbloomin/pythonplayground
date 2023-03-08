# https://developer.yahoo.com/fantasysports/guide/
# create API Key: https://developer.yahoo.com/apps/create/

# https://developer.yahoo.com/apps/hliwrqgw/
# App ID: hliwrqgw
# Client ID (Consumer Key): dj0yJmk9TW1oOFJXVVJLWVo0JmQ9WVdrOWFHeHBkM0p4WjNjbWNHbzlNQT09JnM9Y29uc3VtZXJzZWNyZXQmc3Y9MCZ4PWJi
# Client Secret (Consumer Secret): bc76d281b53b6d257bc63fee8324aebbcf39f78f
# OAuth Required
# https://developer.yahoo.com/oauth2/guide/flows_authcode/
import requests

CLIENT_ID = "dj0yJmk9TW1oOFJXVVJLWVo0JmQ9WVdrOWFHeHBkM0p4WjNjbWNHbzlNQT09JnM9Y29uc3VtZXJzZWNyZXQmc3Y9MCZ4PWJi"
CLIENT_SECRET = "bc76d281b53b6d257bc63fee8324aebbcf39f78f"
REDIRECT_URI = "https://www.stevencbloom.com"

def create_oauth_link():
    params = {
        "client_id": CLIENT_ID,
        "redirect_uri": REDIRECT_URI,
        "scope": "user",
        "response_type": "code",
    }
    endpoint = "https://api.login.yahoo.com/oauth2/request_auth"
    response = requests.get(endpoint, params=params)
    url = response.url
    return url

print(create_oauth_link())