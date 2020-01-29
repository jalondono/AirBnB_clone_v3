#!/usr/bin/python3
"""
this file run the application
"""
from flask import Flask, jsonify
from models import storage
from api.v1.views import app_views
import os

app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def close(zzz):
    """Close"""
    storage.close()


@app.errorhandler(404)
def page_not_found(e):
    """Page not found"""
    return jsonify(error="Not found")


if __name__ == "__main__":
    host = os.environ.get("HBNB_API_HOST")
    port = os.environ.get("HBNB_API_PORT")
    app.run(host=host, port=port, debug=True, threaded=True)
