# https://pypi.org/project/yahoo-oauth/
# https://pypi.org/project/yahoo-fantasy-api/
# https://developer.yahoo.com/fantasysports/guide/


from yahoo_oauth import OAuth2

#connect to yahoo api
oauth = OAuth2(None, None, from_file='oauth2.json')
guid = oauth.guid

if not oauth.token_is_valid():
    oauth.refresh_access_token()

# Example
# response = oauth.session.get(url, params=payload)
response = oauth.session.get('https://fantasysports.yahooapis.com/fantasy/v2/game/nfl')
print(response)