from flask import request, jsonify, Blueprint, g
from flask import abort, make_response
import json

book_blueprint = Blueprint('users', __name__)

@book_blueprint.route('/add_user', methods=['POST'])
def add_book():
    pass

@book_blueprint.route('/get_user/<id>', methods=['POST'])
def get_book(id):
    pass

def delete_book():
    pass