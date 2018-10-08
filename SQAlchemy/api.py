from flask import Flask
from flask_restful import Api

from resources.maintenance_requests import Request, RequestList, Item

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)

@app.before_first_request
def create_tables():
	db.create_all()

api.add_resource(Request, '/request/<string:title>', endpoint = 'Request') # http://localhost:5000/request/<title>
api.add_resource(Item, '/request/<int:req_id>', endpoint = 'Item')
api.add_resource(RequestList, '/requests', endpoint = 'RequestList')

if __name__ == '__main__':
	from db import db
	db.init_app(app)
	app.run(debug=True, port=9)