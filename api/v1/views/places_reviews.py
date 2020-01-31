#!/usr/bin/python3
"""
    Module of blueprints of flask
"""
from models import storage
from api.v1.views import app_views
from flask import jsonify, abort, request
from models.review import Review



@app_views.route("/places/<place_id>/reviews",
                 methods=['GET'], strict_slashes=False)
def show_reviews(place_id):
    """lists all reviews"""
    l_list = []
    look_place = storage.get("Place", place_id)
    if look_place is None:
        abort(404)
    reviews = storage.all("Review")
    for review in reviews.values():
        if place_id == getattr(review, 'place_id'):
            review_list.append(review.to_dict())
    return jsonify(l_list), 200


@app_views.route("reviews/<review_id>", methods=['GET'], strict_slashes=False)
def one_review(review_id):
    """Get a review"""
    r = storage.get("Review", review_id)
    if r is None:
        abort(404)
    return jsonify(r.to_dict())


@app_views.route("reviews/<review_id>",
                 methods=['DELETE'], strict_slashes=False)
def delete_review(review_id):
    """eliminate a review"""
    r = storage.get("Review", review_id)
    if r is None:
        abort(404)
    r.delete()
    storage.save()
    return jsonify({}), 200


@app_views.route("places/<place_id>/reviews",
                 methods=['POST'], strict_slashes=False)
def creates_review(place_id):
    """Creates a Review"""
    data = request.get_json()
    if data is None:
        abort(400, 'Not a JSON')
    elif data.get('user_id') is None:
        abort(400, 'Missing user_id')
    elif data.get('text') is None:
        abort(400, 'Missing text')
    look_state = storage.get("Place", place_id)
    elif look_state is None:
        abort(404)
    look_state = storage.get("User", data.get('user_id'))
    if look_state is None:
        abort(404)
    data['place_id'] = place_id
    new_r = Review(**post_data)
    storage.new(new_r)
    storage.save()
    return jsonify(new_r.to_dict()), 201


@app_views.route("/reviews/<review_id>",
                 methods=['PUT'], strict_slashes=False)
def updates_review(review_id):
    """Updates a review"""
    no_changes= ['id', 'created_at', 'updated_at', 'state_id', 'user_id', 'place_id']
    r = storage.get("Review", review_id)
    if r is None:
        abort(404)
    data = request.get_json()
    if data is None:
        abort(400, 'Not a JSON')
    for key, value in data.items():
        if key in no_changes:
            pass
        else:
            setattr(r, key, value)
    r.save()
    return jsonify(r.to_dict()), 200