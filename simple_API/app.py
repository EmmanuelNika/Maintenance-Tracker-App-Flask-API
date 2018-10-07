from flask import Flask, jsonify, request, render_template, abort
from multiprocessing import Value

app = Flask(__name__)

requests = []

counter = Value('i', 0)

def id_generator():
	with counter.get_lock():
		counter.value += 1
		return counter.value

@app.route('/', methods=['GET'])
def index():
    """Renders a sample page."""
    return render_template('index.html')

# GET /requests 						Fetch all requests
@app.route('/requests', methods=['GET'])
def getAll():
	return jsonify({'requests':requests})

# GET /requests/<requestId> 			Fetch a single request
@app.route('/request/<int:req_id>', methods=['GET'])
def get_request(req_id):
	for request in requests:
		if str(request['id']) == str(req_id):
			return jsonify(request)
	abort(404)

# POST /requests						Create a request
@app.route('/request', methods=['POST'])
def create_request():
	request_data = request.get_json()
	new_request = {
		'id': id_generator(),
		'title': request_data['title'],
		'status': 'In Progress'
	}
	requests.append(new_request)
	return jsonify(new_request), 201

# POST /requests/<string:id>/cleared	Attend to a request
@app.route('/request/<int:req_id>/cleared', methods=['POST'])
def create_title_in_request(req_id):
	request_data = request.get_json()
	for req in requests:
		if str(req['id']) == str(req_id):
			requests[0]['status'] = request.json['status']
			return jsonify(requests), 201
	abort(404)

@app.errorhandler(404)
def page_not_found(e):
	return jsonify({'message': 'request not found'}), 404

@app.errorhandler(405)
def request_not_supported(e):
	return render_template("405.html")

if __name__ == '__main__':
    app.run(debug=True, port=5555)