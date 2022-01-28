from flask import request, jsonify, Blueprint, g, render_template
from flask import abort, make_response
import json
import pickle
import pandas as pd
from api.models.model import Results
from development.common_util.config import modeloutput, rawfields

results_blueprint = Blueprint('usecase', __name__, url_prefix='/usecase')

@results_blueprint.route('/get_data', methods=['GET'])
def get_data():
    t = """
    \n
    <br>
    <br>
    <form action="predict" method="get">

        <button type="submit" class="btn btn-primary btn-block btn-large">Predict</button>
    </form>
    """
    df = pd.read_sql(g.session.query(Results).filter(
        Results.index < 120).statement, g.session.bind)
    output = df.to_html()
    output = output + t
    return render_template("index.html", prediction_text = output)

@results_blueprint.route('/get_results/<id>', methods=['GET'])
def get_results(id):
    result = g.session.get(Results, id)
    return make_response(jsonify(result.as_dict())), 200

@results_blueprint.route('/predict', methods=['GET'])
def predict():
    df = pd.read_sql(g.session.query(Results).filter(
        Results.index < 120).statement, g.session.bind)
    model = pickle.load(open(modeloutput, "rb"))
    df['Class'] = model.predict(df[rawfields])
    return render_template("index.html", prediction_text = df.to_html())

