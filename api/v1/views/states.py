#!/usr/bin/python3
from flask import jsonify, abort, request
from api.v1.views import app_views
from models import storage
from models.state import State


@app_views.route('/states/', methods=['GET'], strict_slashes=False)
def show_states():
    """This functions lists all the states"""
    list_t = []
    states = storage.all("State")
    for state in states.values():
        list_t.append(state.to_dict())
    return jsonify(list_t)


@app_views.route('/states/<state_id>', methods=['GET'], strict_slashes=False)
def get_state(state_id):
    """This functions get a specific state by id"""
    try:
        states = storage.all("State")
        s_id = "State." + state_id
        state = states.get(s_id).to_dict()
        return state
    except Exception:
        abort(404)


@app_views.route('/states/<state_id>', methods=['DELETE'], strict_slashes=False)
def delete_state(state_id):
    """This function delete a state by id"""
    states = storage.all('State')
    s_id = "State." + state_id
    to_del = states.get(s_id)
    if to_del is None:
        abort(404)
    storage.delete(to_del)
    storage.save()
    return jsonify({}), 200


@app_views.route('/states/', methods=['POST'], strict_slashes=False)
def create_state():
    """This function create a new state"""
    data = request.get_json()
    if not data:
        abort(400, 'Not a JSON')
    elif not 'name' in data:
        abort(400, 'Missing name')
    state = State()
    state.name = data['name']
    state.save()
    state = state.to_dict()
    return jsonify(state), 201


@app_views.route('/states/<state_id>', methods=['PUT'], strict_slashes=False)
def update_state(state_id):
    """This function update a state by id"""
    data = request.get_json()
    if not data:
        abort(400, 'Not a JSON')
    s_id = "State." + state_id
    states = storage.all("State")
    if states.get(s_id) is None:
        abort(404)
    else:
        state = states.get(s_id)
    state.name = data['name']
    state.save()
    state = state.to_dict()
    return jsonify(state), 200
