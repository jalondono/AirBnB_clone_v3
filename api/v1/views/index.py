#!/usr/bin/python3
from api.v1.views import app_views
from flask import jsonify
from models import storage


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """ Return Ok status"""
    return jsonify(status='OK')


@app_views.route('/stats', strict_slashes=False)
def count():
    """This function counts the instances of classes"""
    ame = storage.count("Amenity")
    cit = storage.count("City")
    pla = storage.count("Place")
    rev = storage.count("Review")
    sta = storage.count("State")
    user = storage.count("User")
    return jsonify(amenities=ame, cities=cit,
                   places=pla, reviews=rev,
                   states=sta, users=user)
