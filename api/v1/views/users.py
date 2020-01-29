#!/usr/bin/python3
"""
City
"""
from flask import jsonify, abort, request
from api.v1.views import app_views
from models import storage
from models.user import User


@app_views.route('/users', methods=['GET'], strict_slashes=False)
def show_users():
    """This functions lists all the users"""
    list_t = []
    users = storage.all("User")
    for user in users.values():
        list_t.append(user.to_dict())
    return jsonify(list_t)


@app_views.route('/users/<user_id>', methods=['GET'], strict_slashes=False)
def get_user(user_id):
    """This functions get a specific state by id"""
    users = storage.all("User")
    u_id = "User." + user_id
    if users.get(u_id) is None:
        abort(404)
    user = users.get(u_id).to_dict()
    return user


@app_views.route('/users/<user_id>',
                 methods=['DELETE'], strict_slashes=False)
def delete_user(user_id):
    """This function delete a state by id"""
    users = storage.all(User)
    u_id = "User." + user_id
    to_del = users.get(u_id)
    if to_del is None:
        abort(404)
    storage.delete(to_del)
    storage.save()
    return jsonify({}), 200


@app_views.route('/users', methods=['POST'], strict_slashes=False)
def create_user():
    """This function create a new city"""
    data = request.get_json()
    if not data:
        abort(400, 'Not a JSON')
    elif 'email' not in data:
        abort(400, 'Missing email')
    elif 'password' not in data:
        abort(400, 'Missing password')
    user = User()
    user.email = data['email']
    user.password = data['password']
    user.save()
    user = user.to_dict()
    return jsonify(user), 201


@app_views.route('/users/<user_id>', methods=['PUT'], strict_slashes=False)
def update_user(user_id):
    """This function update a state by id"""
    data = request.get_json()
    users = storage.all(User)
    match = 'User.' + user_id
    if users.get(match) is None:
        abort(404)
    if not data:
        abort(400, 'Not a JSON')
    else:
        user = users.get(match)
        user.password = data['password']
        user.save()
        user = user.to_dict()
    return jsonify(user), 200
