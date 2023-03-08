# Flask example
# https://flask.palletsprojects.com/en/2.2.x/
# in terminal, run:
#    flask --app .\my_python_example.py run
# ---> runs on local server
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'Hello, World'