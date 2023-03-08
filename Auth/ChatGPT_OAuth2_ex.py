import requests

# API endpoint to retrieve all current NFL players
endpoint = "https://api.nfl.com/v1/players/positions"

# Define query parameters to retrieve running backs
params = {
    "positionIds": "2",  # 2 corresponds to running back position
    "teamIds": "",  # Leave empty to retrieve all running backs regardless of team
    "sort": "ASC"  # Sort the players in ascending order of their last names
}

# Replace "YOUR_API_KEY_HERE" with your actual API key
headers = {
    "Authorization": f"Bearer YOUR_API_KEY_HERE"
}

# Make a GET request to the endpoint with the specified parameters and headers
response = requests.get(endpoint, params=params, headers=headers)

# If the request was successful (status code 200), retrieve the player data from the response
if response.status_code == 200:
    data = response.json()
    running_backs = data["players"]
    # Process the running back data
else:
    print(f"Error retrieving data: {response.status_code}")