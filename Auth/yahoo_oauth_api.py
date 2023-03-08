# https://pypi.org/project/yahoo-oauth/
# https://pypi.org/project/yahoo-fantasy-api/

from yahoo_oauth import OAuth2
import yahoo_fantasy_api as yfa

#connect to yahoo api
sc = OAuth2(None, None, from_file='oauth2.json')

#get game object
gm = yfa.Game(sc, 'nfl')
leagues = gm.league_ids()
# print(leagues) # ['348.l.535112', '359.l.676495', '371.l.285372', '380.l.979173', '390.l.789076', '406.l.1123078', '414.l.1014170']

lg = gm.to_league(leagues[0])

print(lg.stat_categories())
print(lg.team_key())

tm = lg.to_team(lg.team_key())
print(tm.roster())
