from flask import Blueprint, jsonify, request
from src.services.expanses_service import query_data
from flask import Blueprint

expanses_route = Blueprint('expanses_data', __name__)


@expanses_route.route('/', methods=['GET'])
def query():
    params = request.args.to_dict()
    results = query_data(params)
    return jsonify(results)



