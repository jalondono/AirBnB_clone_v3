#!/usr/bin/python3
"""
Amenity
"""
from flask import jsonify, abort, request
from api.v1.views import app_views
from models import storage
from models.amenity import Amenity


@app_views.route('/amenities', methods=['GET'], strict_slashes=False)
def show_amenity():
    """This functions lists all the amenities"""
    list_t = []
    amenities = storage.all("Amenity")
    for amenity in amenities.values():
        list_t.append(amenity.to_dict())
    return jsonify(list_t)


@app_views.route('/amenities/<amenity_id>',
                 methods=['GET'], strict_slashes=False)
def get_amenity_id(amenity_id):
    """This functions get a specific state by id"""
    amenities = storage.all("Amenity")
    c_id = "Amenity." + amenity_id
    if amenities.get(c_id) is None:
        abort(404)
    amenity = amenities.get(c_id).to_dict()
    return amenity


@app_views.route('/amenities/<amenity_id>',
                 methods=['DELETE'], strict_slashes=False)
def delete_amenity(amenity_id):
    """This function delete a state by id"""
    amenities = storage.all('Amenity')
    c_id = "Amenity." + amenity_id
    to_del = amenities.get(c_id)
    if to_del is None:
        abort(404)
    storage.delete(to_del)
    storage.save()
    return jsonify({}), 200


@app_views.route('/amenities',
                 methods=['POST'], strict_slashes=False)
def create_amenity():
    """This function create a new amenity"""
    data = request.get_json()
    if not data:
        abort(400, 'Not a JSON')
    elif 'name' not in data:
        abort(400, 'Missing name')
    amenity = Amenity()
    amenity.name = data['name']
    amenity.save()
    amenity = amenity.to_dict()
    return jsonify(amenity), 201


@app_views.route('/amenities/<amenity_id>',
                 methods=['PUT'], strict_slashes=False)
def update_amenity(amenity_id):
    """This function update a state by id"""
    data_dic = request.get_json()
    amenities = storage.all('Amenity')
    match = 'Amenity.' + amenity_id
    if amenities.get(match) is None:
        abort(404)
    if not data_dic:
        abort(400, 'Not a JSON')
    else:
        amenity = amenities.get(match)
        for key, value in data_dic.items():
            if key != "id" and key != "created_at" and key != "updated_at":
                setattr(amenity, key, value)
        amenity.save()
        amenity = amenity.to_dict()
    return jsonify(amenity), 200
