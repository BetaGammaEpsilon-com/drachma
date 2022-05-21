from flask import Blueprint

home_bp = Blueprint('home', __name__, url_prefix='')

@home_bp.route('/')
def index():
    return 'Home'

@home_bp.route('/version')
def version():
    return 'Version'