from flask import Flask, request, abort
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class Offer(Resource):
    def __init__(self):
        self.id = request.headers.get('user-id')
        if not self.id:
            abort(403)

    def get(self):
        id = request.headers.get('user-id')
        return {'get': id}

    def put(self):
        id = request.headers.get('user-id')
        return {'put': id}

api.add_resource(Offer, '/offer/')


if __name__ == '__main__':
    app.run(debug=True)
