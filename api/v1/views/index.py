#!/usr/bin/python3
from api.v1.views import app_views
from flask import jsonify
from models import storage
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


@app_views.route('/status', methods=['GET'])
def status():
    return jsonify(status='OK')


@app_views.route('/stats')
def count():
    ame = storage.count(Amenity)
    cit = storage.count(City)
    pla = storage.count(Place)
    rev = storage.count(Review)
    sta = storage.count(State)
    user = storage.count(User)
    return jsonify(amenities=ame, cities=cit,
                   places=pla, reviews=rev,
                   states=sta, users=user)
