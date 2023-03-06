# Python API example
# https://realpython.com/python-api/
import requests
# response = requests.get("https://api.thedogapi.com/v1/breeds")
# x = requests.get("https://randomuser.me/api/")
# print(x)        # <Response [200]>
# print(x.text)   # {"results":[{"gender":"male","name":{"title":"Mr","first":"Ronnie",
# response = requests.get("https://api.thedogapi.com/v1/breeds")

# print(response)             # <Response [200]>
# print(response.request)     # <PreparedRequest [GET]>
# request = response.request  # shorten
# print(request.url)          # 'https://api.thedogapi.com/v1/breeds'
# print(request.path_url)     # /v1/breeds
# print(request.method)       # 'GET'
# print(request.headers)      # {'User-Agent': 'python-requests/2.24.0', 'Accept-Encoding': 'gzip, deflate'...
# print(response.status_code)
# print(response.reason)
# print(response.headers)
# print(response.cookies.keys())
# print(response.headers.get("Content-Type"))  # application/json; charset=utf-8
# print(response.content)


# print(response.headers.get("Content-Type"))
# print(response.json())
# json_response = response.json()
# print(json_response[1]["name"])

# query parameters
# query_params = {"q": "labradoodle"}
# endpoint = "https://api.thedogapi.com/v1/breeds/search"
# print(requests.get(endpoint, params=query_params).json())

endpoint2 = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos"
api_key = "DEMO_KEY"
query_params2 = {"api_key": api_key, "earth_date": "2020-07-01"}
response = requests.get(endpoint2, params=query_params2)
print(response)
photos = response.json()["photos"]
print(f"Found {len(photos)} photos")
print(photos[4]["img_src"])
