from flask import Blueprint
from models.base_model import BaseModel

bmodel = BaseModel
app_views = Blueprint('app_views', __name__)
from api.v1.views.states import *
from api.v1.views.index import *

