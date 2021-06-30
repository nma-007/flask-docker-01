
from flask import Blueprint
from flask import make_response, redirect, render_template, request, url_for, jsonify

api = Blueprint('api', __name__)

@api.route('/api/data', methods = ['GET'])
def names():
	data = {"names": ["John", "Jacob", "Julie", "Jennifer"]}
	return jsonify(data)