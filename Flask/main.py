# Flask RESTful API demo
# based on @timeoutwithtim youtube
from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

names = {"tim": {"age": 19, "gender": "male"},
        "bill": {"age": 70, "gender": "male"}}

class HelloWorld(Resource):
    def get(self, name):
        return names[name]

    def post(self):
        return {"test": "Posted"}


api.add_resource(HelloWorld, "/helloworld/<string:name>")
# api.add_resource(HelloWorld, "/helloworld")

if __name__ == "__main__":
    app.run(debug=True)  # turn off in production environment
