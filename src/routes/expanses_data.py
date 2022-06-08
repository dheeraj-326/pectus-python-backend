from flask import Blueprint, jsonify
from src.services.expanses_service import get_all

expanses_data_route = Blueprint('expanses_data', __name__)


@expanses_data_route.route('/')
def fetch_all():
    return jsonify(get_all())

