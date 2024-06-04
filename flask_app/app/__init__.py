from flask import Flask
from dotenv import load_dotenv
import os
import pkgutil
from app.services.azure_service import initialize_azure_embedding, initialize_azure_openai
from app.services.elasticsearch_service import get_elastic_retriever

def create_app():
    load_dotenv()
    app = Flask(__name__)
    
    # Load configuration from config.py
    app.config.from_object('app.config.Config')
    initialize_azure_openai()
    initialize_azure_embedding()
    app.elasticsearch_retriever = get_elastic_retriever()

    # Dynamically register blueprints
    register_blueprints(app)
    
    return app

def register_blueprints(app):
    import app.routes as routes_package
    package_dir = os.path.dirname(routes_package.__file__)
    for _, module_name, _ in pkgutil.iter_modules([package_dir]):
        module = __import__(f'app.routes.{module_name}', fromlist=[module_name])
        if hasattr(module, 'blueprint'):
            app.register_blueprint(module.blueprint)
