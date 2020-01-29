#!/usr/bin/python3
from flask import Flask, jsonify
from models import storage
from api.v1.views import app_views
import os

app = Flask(__name__)
app.url_map.strict_slashes = False
app.register_blueprint(app_views, url_prefix='/api/v1')


@app.teardown_appcontext
def close(zzz):
    storage.close()


@app.errorhandler(404)
def page_not_found(e):
    return jsonify(error="Not found")


if __name__ == "__main__":
    host = os.environ.get("HBNB_API_HOST")
    port = os.environ.get("HBNB_API_PORT")
    app.run(host=host, port=port, debug=True, threaded=True)
