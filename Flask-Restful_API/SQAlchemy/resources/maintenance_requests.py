from flask import Flask, request, jsonify, make_response, abort
from flask_restful import Resource, reqparse
from multiprocessing import Value
from models.maintenance_requests import RequestModel

class Request(Resource):
	parser = reqparse.RequestParser()
	parser.add_argument('price',
		type=float,
		required=True,
		)
	parser.add_argument('status',
		type=str,
		required=True,
		)

	def get(self, title):
		request_item = RequestModel.find_by_title(title)
		if request_item:
			return request_item.json()
		return {"Message": 'Item not found'}, 404

	def post(self, title):

		if RequestModel.find_by_title(title):
			return {"Message": "A request with that title already exists"}, 400

		data = Request.parser.parse_args()

		request_item = RequestModel(title, data['status'], data['price'])
		
		try:
			request_item.save_to_db()
		except:
			return {"Message": "An error occurred inserting the request."}, 500
		
		return request_item.json(), 201

	def delete(self, title):
		request_item = RequestModel.find_by_title(title)
		if request_item:
			request_item.delete_from_db()

		return {"Message": "Request has been deleted."}

	def put(self, title):
		data = Request.parser.parse_args()

		request_item = RequestModel.find_by_title(title)
		
		if request_item is None:
			request_item = RequestModel(title, data['status'], data['price'])
		else:
			request_item.status = data['status']
			request_item.price = data['price']

		request_item.save_to_db()

		return request_item.json(), 201

class RequestList(Resource):
	def get(self):
		return {'Requests': [request_item.json() for request_item in RequestModel.query.all()]}

class Item(Resource):

	def get(self, req_id):
		request_item = RequestModel.find_by_id(req_id)
		if request_item:
			return request_item.json()
		return {"Message": 'Item not found'}, 404
				
	def delete(self, req_id):
		global requests
		requests = list(filter(lambda x: x['req_id'] != req_id, requests))
		return {'message': 'Request deleted'}

	def put(self, req_id):
		data = Request.parser.parse_args()

		request_item = RequestModel.find_by_id(req_id)
		
		if request_item is None:
			request_item = RequestModel(title, data['status'], data['price'])
		else:
			request_item.status = data['status']
			request_item.price = data['price']

		request_item.save_to_db()

		return request_item.json(), 201

