#!/usr/bin/python3
from flask import Flask, jsonify
from models import storage
from api.v1.views import app_views

app = Flask(__name__)
app.register_blueprint(app_views, url_prefix='/api/v1')

@app.teardown_appcontext
def close(zzz):
    storage.close()

@app.errorhandler(404)
def page_not_found(e):
    return jsonify(error="Not found")

if __name__ == "__main__":
    app.run(debug=True, threaded=True)