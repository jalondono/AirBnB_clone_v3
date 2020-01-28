from api.v1.views import app_views, bmodel
from flask import jsonify
from models import storage


@app_views.route('/states/')
def get_states():
    a = []
    states = storage.all('State')
    for state in states.values():
        a.append(bmodel.to_dict(state))
    return jsonify(a)
