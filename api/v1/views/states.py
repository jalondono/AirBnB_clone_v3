#!/usr/bin/python3
from flask import jsonify
from api.v1.views import app_views
from models import storage

@app_views.route('/states/', methods=['GET'])
def show_states():
    list_t = []
    states = storage.all("State")
    for state in states.values():
        list_t.append(state.to_dict())
    return jsonify(list_t)
