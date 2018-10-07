from flask import Flask
from flask_restful import Api

from resources.maintenance_requests import Request, RequestList, Item

app = Flask(__name__)
api = Api(app)

api.add_resource(Request, '/request/<string:title>', endpoint = 'Request') # http://localhost:5000/request/<title>
api.add_resource(Item, '/request/<int:req_id>', endpoint = 'Item')
api.add_resource(RequestList, '/requests', endpoint = 'RequestList')

if __name__ == '__main__':
	app.run(debug=True, port=8)