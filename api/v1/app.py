#!/usr/bin/python3
"""
starts a Flask web application
"""
import os
from flask import Flask
from models import storage
from api.v1.views import app_views
from flask import jsonify

app = Flask(__name__)
app.register_blueprint(app_views, url_prefix='/api/v1/')


@app.teardown_appcontext
def teardown(exe):
    storage.close()


@app_views.errorhandler(404)
def pag_not_found(err):
    """definition of error handler"""
    return jsonify({"error": "Not found"})


if __name__ == "__main__":
    host = os.environ.get('HBNB_API_HOST')
    port = os.environ.get('HBNB_API_PORT')
    app.run(debug=True)
