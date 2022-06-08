from flask import Blueprint, redirect, request
from sqlite3 import IntegrityError

from api.logic.select import *
from api.logic.user import logic_get_user_info, logic_create_user, logic_get_users
from api.logic.transaction import logic_add_tx
from api.util.response import format_json
from api.util.error import bad_request_error

URL_PREFIX = '/user'
user_bp = Blueprint('user', __name__, url_prefix=URL_PREFIX)

@user_bp.route('', methods=['GET', 'POST'])
def route_user():
    """
    On `GET`: Returns all Users
    On `POST`: Creates a User

    Returns:
        dict: Response packet
    """
    if request.method == 'GET':
        return format_json(logic_get_users())
    elif request.method == 'POST':
        try:
            return format_json(logic_create_user(request))
        except KeyError:
            return format_json(bad_request_error('Error in creating new user -- request must include `name` and `balance` fields.'), status=400)
        except IntegrityError:
            return format_json(bad_request_error('`name` parameter must be unique.'), status=403)

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
    
    Args:
        uid (int): The UID of the User to add the transaction to.
    """
    try:
        return format_json(logic_add_tx(request, uid=uid))
    except KeyError:
        # one of the parameters wasn't passed: send Bad Request 400
        return format_json(bad_request_error(f'POST to /user/{uid}/tx did not contain necessary fields: `price`, `motion`, `description`'), status=400)