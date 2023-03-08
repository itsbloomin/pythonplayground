import requests
from requests_oauthlib import OAuth2Session
from oauthlib.oauth2 import BackendApplicationClient

# Define API endpoints and credentials
token_url = 'https://api.login.yahoo.com/oauth2/request_auth'
api_url = 'https://fantasysports.yahooapis.com/fantasy/v2/game/nfl'

client_id = 'dj0yJmk9R29Jek9GcjBQMEdzJmQ9WVdrOWExVkhhbWcyYUhNbWNHbzlNQT09JnM9Y29uc3VtZXJzZWNyZXQmc3Y9MCZ4PTBk'
client_secret = '5eb1f31e434264055de63041fb4a6c42e3d8039a'

# Create an OAuth2Session object with a BackendApplicationClient
client = BackendApplicationClient(client_id=client_id)
oauth = OAuth2Session(client=client)

# Fetch an access token using the client credentials grant
token = oauth.fetch_token(token_url=token_url, client_id=client_id,
                          client_secret=client_secret)

# Make an authenticated request to the API using the access token
headers = {'Authorization': f'Bearer {token["access_token"]}'}
response = requests.get(api_url, headers=headers)

if response.status_code == 200:
    data = response.json()
    # Process the response data
else:
    print(f'Error: {response.status_code}')