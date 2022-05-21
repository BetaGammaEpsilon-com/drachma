from flask import Blueprint, jsonify, redirect, url_for

from app.logic.select import *

URL_PREFIX = '/user'
user_bp = Blueprint('user', __name__, url_prefix=URL_PREFIX)

@user_bp.route('/<int:uid>')
def display(uid):
    """
    Returns the list of transactions for user with given uid.
    
    Args:
        uid (int): The UID of the User to pull
    """
    # TODO abstract
    user = get_user_by_uid(uid)
    user_dict = user.serialize()
    user_dict['tx'] = get_transactions_by_uid(uid)
    return jsonify(user_dict)

@user_bp.route('/<string:name>')
def redirect_to_display(name):
    """
    Pull UID for given name, if exists, and route to /user/<uid>

    Args:
        name (string): The User's name to pull
    """    
    # get UID from name
    uid = get_uid_by_name(name)
    return redirect(f'{URL_PREFIX}/{uid}')