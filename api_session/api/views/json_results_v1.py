from flask import request, jsonify, Blueprint, g
from flask import make_response
from api.models.model import Results

api_blueprint = Blueprint('apiv1', __name__, url_prefix='/api/v1')

@api_blueprint.route('/get_results/<id>', methods=['GET'])
def get_results_api_v1(id):
    result = g.session.get(Results, id)
    return make_response(jsonify(result.as_dict())), 200
