# Flask RESTful API demo
# based on @timeoutwithtim youtube
from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return ({"item" : "Hello World"})

    def post(self):
        return ({"test" : "Posted"})

api.add_resource(HelloWorld, "/helloworld")

if __name__ == "__main__":
    app.run(debug=True)  # turn off in production environment
