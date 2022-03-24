import os
import atexit
from flask import Flask, config, g, send_from_directory, render_template
from api.resources.config import *
from flask_swagger_ui import get_swaggerui_blueprint
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, session, sessionmaker
from api.views.results import results_blueprint
from api.views.json_results_v1 import api_blueprint as api_blueprint_v1
from api.views.json_results_v2 import api_blueprint as api_blueprint_v2
from api.models.model import Base


app = Flask(__name__, template_folder='templates')


@app.route('/hello/', methods=['GET', 'POST'])
def welcome():
    return render_template("index.html")


engine = create_engine("sqlite:///data.db")
db = scoped_session(sessionmaker(bind=engine))
Base.metadata.create_all(engine)

@app.route("/static")
def send_static():
    return send_from_directory("static", "swagger.yaml")

SWAGGER_URL = '/swagger'
API_URL = '/static'
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(SWAGGER_URL,
                                              API_URL,
                                              config = {
                                                  'app_name':"Insights"
                                              })

app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)
app.register_blueprint(results_blueprint)
app.register_blueprint(api_blueprint_v1)
app.register_blueprint(api_blueprint_v2)


def on_exit():
    engine.dispose()
    print("Exit Flask application")

atexit.register(on_exit)

@app.before_request
def before_request():
    g.session = db()

@app.teardown_request
def close_connection(error):
    g.session.close()





