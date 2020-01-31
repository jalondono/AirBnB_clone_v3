#!/usr/bin/python3
"""
City
"""
from flask import jsonify, abort, request
from api.v1.views import app_views
from models import storage
from models.place import Place


@app_views.route('/cities/<city_id>/places', methods=['GET'], strict_slashes=False)
def show_places(city_id):
    """This functions lists all the users"""
    list_t = []
    cities = storage.all("City")
    c_id = "City." + city_id
    if cities.get(c_id) is None:
        abort(404)
    else:
        places = storage.all("Place")
        for place in places.values():
            if place.city_id == city_id:
                list_t.append(place.to_dict())
    return jsonify(list_t)

@app_views.route('places/<place_id>', methods=['GET'], strict_slashes=False)
def get_place(place_id):
    """This functions get a specific state by id"""
    places = storage.all("Place")
    p_id = "Place." + place_id
    if places.get(p_id) is None:
        abort(404)
    place = places.get(p_id).to_dict()
    return place


@app_views.route('/places/<place_id>',
                 methods=['DELETE'], strict_slashes=False)
def delete_place(place_id):
    """This function delete a state by id"""
    places = storage.all(Place)
    p_id = "Place." + place_id
    to_del = places.get(p_id)
    if to_del is None:
        abort(404)
    storage.delete(to_del)
    storage.save()
    return jsonify({}), 200


@app_views.route('/cities/<city_id>/places', methods=['POST'], strict_slashes=False)
def create_place(city_id):
    """This function creates a new place"""
    data = request.get_json()
    cities = storage.all("City")
    c_id = "City." + city_id
    if cities.get(c_id) is None:
        abort(404)
    if not data:
        abort(400, 'Not a JSON')
    elif 'user_id' not in data:
        abort(400, 'Missing user_id')
    u_id = data['user_id']
    look_user = storage.get("User", u_id)
    if look_user is None:
        abort(404)
    elif 'name' not in data:
        abort(400, 'Missing name')
    place = Place()
    place.city_id = data['city_id']
    place.email = data['name']
    place.user_id = data['user_id']
    place.save()
    place = place.to_dict()
    return jsonify(place), 201


@app_views.route('/places/<place_id>', methods=['PUT'], strict_slashes=False)
def update_place(place_id):
    """This function update a state by id"""
    data = request.get_json()
    places = storage.all("Place")
    p_id = "Place." + place_id
    if places.get(p_id) is None:
        abort(404)
    if not data:
        abort(400, 'Not a JSON')
    else:
        place = places.get(p_id)
        for key, value in data.items():
            if key != "id" and key != "created_at" \
                    and key != "updated_at" and key != 'city_id'\
                    and key != "user_id":
                setattr(place, key, value)
        place.save()
        place = place.to_dict()
    return jsonify(place), 200
