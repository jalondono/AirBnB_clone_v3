from api.v1.views import app_views
from flask import jsonify
from models import storage


@app_views.route('/status/')
def status():
    return jsonify({'status': "OK"})


@app_views.route('/stats')
def stats():
    """
    return the number of specific objects
    """
    data = {"amenities": 0, "cities": 0, "places": 0,
            "reviews": 0, "states": 0, "users": 0}
    objects = storage.all()
    for obj in objects.keys():
        a = obj.split('.')
        if a[0] == 'Amenity':
            data['amenities'] += 1
        elif a[0] == 'City':
            data['cities'] += 1
        elif a[0] == 'Place':
            data['places'] += 1
        elif a[0] == 'Review':
            data['reviews'] += 1
        elif a[0] == 'State':
            data['states'] += 1
        elif a[0] == 'User':
            data['users'] += 1
        else:
            pass
    return jsonify(data)

