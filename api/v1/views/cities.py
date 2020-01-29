#!/usr/bin/python3
"""
City
"""
from flask import jsonify, abort, request
from api.v1.views import app_views
from models import storage
from models.state import State


@app_views.route('/states/<state_id>/cities', methods=['GET'], strict_slashes=False)
def show_cities(state_id):
    """This functions lists all the cities"""
    list_t = []
    states = storage.all("State")
    s_id = "State." + state_id
    if states.get(s_id) is None:
        abort(404)
    else:
        cities = storage.all("City")
        for city in cities.values():
            if city['state_id'] == state_id:
                list_t.append(city.to_dict())
    return jsonify(list_t)


@app_views.route('/states/<state_id>', methods=['GET'], strict_slashes=False)
def get_city(state_id):
    """This functions get a specific state by id"""
    try:
        states = storage.all("State")
        s_id = "State." + state_id
        state = states.get(s_id).to_dict()
        return state
    except Exception:
        abort(404)


@app_views.route('/states/<state_id>',
                 methods=['DELETE'], strict_slashes=False)
def delete_city(state_id):
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
def create_city():
    """This function create a new state"""
    data = request.get_json()
    if not data:
        abort(400, 'Not a JSON')
    elif 'name' not in data:
        abort(400, 'Missing name')
    state = State()
    state.name = data['name']
    state.save()
    state = state.to_dict()
    return jsonify(state), 201


@app_views.route('/states/<state_id>', methods=['PUT'], strict_slashes=False)
def update_city(state_id):
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