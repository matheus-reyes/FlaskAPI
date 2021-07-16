from flask import Blueprint
routes = Blueprint('routes', __name__)

from .game import *
from .user import *
