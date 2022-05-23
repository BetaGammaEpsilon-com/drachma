from flask import Blueprint, redirect, request
from flask.json import loads

from app.logic.select import *
from app.db_functions.db_operations import *

from app.logic.user import logic_get_user_info, logic_user_add_tx
from app.util.response import format_json
from app.util.error import bad_request_error

URL_PREFIX = '/user'
user_bp = Blueprint('user', __name__, url_prefix=URL_PREFIX)

@user_bp.route('/<int:uid>')
def route_user_info(uid):
    """
    Returns the list of transactions for user with given uid.
    
    Args:
        uid (int): The UID of the User to pull
    """
    return format_json(logic_get_user_info(uid))

@user_bp.route('/<uid>/tx', methods=['POST'])
def route_user_add_tx(uid):
    """
    Adds a transaction under the User's name. Only adds to the unverified table.
    Request payload should have all necessary parameters.
    
    Args:
        uid (int): The UID of the User to add the transaction to.
    """
    try:
        return format_json(logic_user_add_tx(uid, request))
    except KeyError:
        # one of the parameters wasn't passed: send Bad Request 400
        return format_json(bad_request_error(f'POST to /user/{uid}/tx did not contain necessary headers: price, motion, description'), status=400)

# robert-chatterton: TODO - this might be useless as is. Might keep to simply return UID?
@user_bp.route('/<string:name>') 
def redirect_to_user_info(name):
    """
    Pull UID for given name, if exists, and route to /user/<uid>

    Args:
        name (string): The User's name to pull
    """
    uid = get_uid_by_name(name)
    return redirect(f'{URL_PREFIX}/{uid}')