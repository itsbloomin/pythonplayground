# my_json_examples.py

import json

# some JSON
x = '{ "name":"John", "age":30, "city":"New York"}'

# parse x
y = json.loads(x)

# the result is a python Dictionary
print(y["age"])