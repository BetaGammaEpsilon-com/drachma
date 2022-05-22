from flask import Blueprint, redirect, request
from flask.json import loads

from app.logic.select import *
from app.db_functions.db_operations import *
from app.util.response import format_json

URL_PREFIX = '/user'
user_bp = Blueprint('user', __name__, url_prefix=URL_PREFIX)

@user_bp.route('/<int:uid>')
def list_user_info(uid):
    """
    Returns the list of transactions for user with given uid.
    
    Args:
        uid (int): The UID of the User to pull
    """
    # TODO abstract to logic
    user = get_user_by_uid(uid)
    user_dict = user.serialize()
    user_dict['tx'] = get_transactions_by_uid(uid)
    return format_json(user_dict)

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

@user_bp.route('/<uid>/tx', methods=['POST'])
def add_transaction(uid):
    """
    Adds a transaction under the User's name. Only adds to the unverified table.
    Request payload should have all necessary parameters.
    
    Args:
        uid (int): The UID of the User to add the transaction to.
    """
    try:
        req_body = loads(request.data)
        price = req_body['price']
        motion = req_body['motion']
        description = req_body['description']
    except KeyError:
        # one of these wasn't passed: redirect to base page
        return format_json({
            'error': f'`POST` to `/user/{uid}/tx` did not contain necessary headers: `price`, `motion`, `description`'}, 
            status=400)
    
    if motion == '':
        motion = 'NULL'
    if description == '':
        description = 'NULL'
        
    tx = Transaction(uid, price, 0, motion=motion, description=description)
    insert('tx_unverified', tx)
    return format_json({'message': f'{tx} added by User {uid}'})