from flask import jsonify
from app.services.llama_service import process_query
from llama_index.core import Settings

def query_llama(request):
    data = request.get_json()
    query_text = data.get('prompt')
    if not query_text:
        return jsonify({
            "status": False,
            "message": "Prompt is required",
            "data": None
        }), 400
    
    response_data = process_query(query_text)
    return jsonify(response_data)
