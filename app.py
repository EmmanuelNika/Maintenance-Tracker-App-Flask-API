from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

requests = [
	{
		'name': 'Maintenance Requests',
		'requests' : [
			{
				'req_id': '01',
				'title': 'Replace battery'
			}
		]
	}
]

@app.route('/', methods=['GET'])
def test():
    """Renders a sample page."""
    return render_template('index.html')

# GET /requests 						Fetch all requests
@app.route('/requests', methods=['GET'])
def getAll():
	return jsonify({'requests':requests})

# GET /requests/<name> 			Fetch a single request by name
@app.route('/requests/<string:name>', methods=['GET'])
def get_request(name):
	for request in requests:
		if request['name'] == name:
			return jsonify(request)
	return jsonify({'message':'request not found'})

# GET /requests/<name>/requests			Fetch a request item
@app.route('/requests/<string:name>/requests', methods=['GET'])
def get_request_in_requests(name):
	for request in requests:
		if request['name'] == name:
			return jsonify({'requests': request['requests']})
	return jsonify({'message':'request not found'})

"""
# GET /requests/<requestId>/title		Fetch a request item
@app.route('/requests/<string:req_id>/title', methods=['GET'])
def get_title_in_request(req_id):
	for request in requests:
		if request['req_id'] == req_id:
			return jsonify({'title': request['title']})
	return jsonify({'message':'request not found'})
"""
	
# POST /requests						Create a request
@app.route('/requests', methods=['POST'])
def create_request():
	request_data = request.get_json()
	new_request = {
		'name': request_data['name'],
		'requests': []
	}
	requests.append(request_data)
	return jsonify(new_request)

# POST /requests/<string:id>/request	Create a request
@app.route('/requests/<string:name>/requests', methods=['POST'])
def create_title_in_request(name):
	request_data = request.get_json()
	for req in requests:
		if req['name'] == name:
			new_request = {
				'req_id': request_data['req_id'],
				'title': request_data['title']
			}
			req['requests'].append(request_data)
			return jsonify(new_request)
	return jsonify({'message': 'request not found'})

# POST /requests/<requestId>cleared	Attend to a request
@app.route('/requests/<string:req_id>cleared', methods=['PUT'])
def update_request(req_id):
	pass

if __name__ == '__main__':
    app.run(debug=True, port=5000)