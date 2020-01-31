#!/usr/bin/python3
"""
this file run the application
"""
from flask import Flask, jsonify
from flask_cors import CORS
from models import storage
import os
from api.v1.views import app_views

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "0.0.0.0"}})
app.register_blueprint(app_views)


@app.teardown_appcontext
def close(zzz):
    """Close"""
    storage.close()


@app.errorhandler(404)
def page_not_found(e):
    """Page not found"""
    return jsonify(error="Not found"), 404


if __name__ == "__main__":
    host = os.environ.get("HBNB_API_HOST")
    port = os.environ.get("HBNB_API_PORT")
    app.run(host=host, port=port, debug=True, threaded=True)
