from flask import Flask
from .extensions import api
from .resources import ns
# from flask_cors import CORS # Для REACT

def create_app():
    app = Flask(__name__)
    api.init_app(app)
    api.add_namespace(ns)
    # CORS(app) #Для REACT


    return app