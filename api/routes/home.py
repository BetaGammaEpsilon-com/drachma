from flask import Blueprint

from api.util.response import format_json

URL_PREFIX = ''
home_bp = Blueprint('home', __name__, url_prefix='')

VERSION = '0.3'

@home_bp.route('/')
def index():
    return format_json([])

@home_bp.route('/version')
def version():
    return format_json({'version': VERSION})