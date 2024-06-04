from flask import Blueprint, request
from app.controllers.llama_controller import query_llama

blueprint = Blueprint('api', __name__, url_prefix='/api')

@blueprint.route('/chat', methods=['POST'])
def query_llama_route():
    return query_llama(request)
