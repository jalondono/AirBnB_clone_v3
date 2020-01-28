#!/usr/bin/python3
from flask import jsonify, abort, request
from api.v1.views import app_views
from models import storage


@app_views.route('/states/', methods=['GET'])
def show_states():
    list_t = []
    states = storage.all("State")
    for state in states.values():
        list_t.append(state.to_dict())
    return jsonify(list_t)


@app_views.route('/states/<state_id>', methods=['GET'])
def get_state(state_id):

    try:
        states = storage.all("State")
        s_id = "State." + state_id
        state = states.get(s_id).to_dict()
        return state
    except Exception:
        abort(404)

@app_views.route('/states/<state_id>', methods=['DELETE'])
def delete_state(state_id):
    try:
        states = storage.all('State')
        s_id = "State." + state_id
        to_del = states.get(s_id)
        del to_del
        storage.save()
        return jsonify({})
    except Exception:
        abort(404)

@app_views.route('/states', methods=['POST'])
def create_state():
    if not request.json:
        abort(400, 'Not a JSON')
    elif not 'name' in request.json:
        abort(400, 'Missing name')
    state =