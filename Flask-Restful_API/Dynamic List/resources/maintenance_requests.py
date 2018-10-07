from flask import Flask, request, jsonify, make_response, abort
from flask_restful import Resource
from multiprocessing import Value

requests = []

counter = Value('i', 0)

def id_generator():
	with counter.get_lock():
		counter.value += 1
		return counter.value

class Request(Resource):

	def get(self, title):
		for request in requests:
			if request['title'] == title:
				return jsonify(request)
		abort(404, 'The requested URL was not found')

	def post(self, title):
		request_data = request.get_json()

		new_request = {
			'req_id': id_generator(),
			'title': title,
			'status': request_data['status'],
			'price': request_data['price']
		}
		requests.append(new_request)
		return make_response(jsonify(new_request), 201)

	def delete(self, title):
		global requests
		requests = list(filter(lambda x: x['title'] != title, requests))
		return {'message': 'Request deleted'}

	def put(self, title):
		data = request.get_json()
		req = next(iter(filter(lambda x: x['title'] == title, requests)), None)
		if req is None:
			req = {'title': data['title'], 'status': data['status']}
			requests.append(req)
		else:
			req.update(data)
		return req

class RequestList(Resource):
	def get(self):
		return jsonify({'Requests': requests})

class Item(Resource):

	def get(self, req_id):
		for request in requests:
			if request['req_id'] == req_id:
				return jsonify(request)
		abort(404, 'The requested URL was not found')

	def delete(self, req_id):
		global requests
		requests = list(filter(lambda x: x['req_id'] != req_id, requests))
		return {'message': 'Request deleted'}

	def put(self, req_id):
		data = request.get_json()
		req = next(iter(filter(lambda x: x['title'] == title, requests)), None)
		if req is None:
			req = {'title': data['title'], 'status': data['status']}
			requests.append(req)
		else:
			req.update(data)
		return req	

