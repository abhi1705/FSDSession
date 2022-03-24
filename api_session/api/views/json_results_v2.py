from flask import request, jsonify, Blueprint, g
from flask import make_response
from api.models.model import Results


api_blueprint = Blueprint('apiv2', __name__, url_prefix='/api/v2')

@api_blueprint.route('/get_results/<id>', methods=['GET'])
def get_results_api_v1(id):
    result = g.session.get(Results, id)
    return make_response(jsonify(result.as_dict())), 200

@api_blueprint.route('/train', methods=['POST'])
def train_model():
    if not request.json or not 'method' in request.json:
        return make_response(jsonify("'method' not specified")), 400
    else:
        method = request.json['method']
    return make_response(jsonify(f"Retraining Model using '{method}'...")), 200