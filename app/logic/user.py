from flask.json import loads

from app.logic.select import get_user_by_uid, get_transactions_by_uid
from app.models.transaction import Transaction
from app.db_functions.db_operations import insert

def logic_get_user_info(uid):
    """
    Returns the list of transactions for user with given uid.
    
    Args:
        uid (int): The UID of the User to pull
    """
    user = get_user_by_uid(uid)
    user_dict = user.serialize()
    user_dict['tx'] = get_transactions_by_uid(uid)
    return user_dict

def logic_user_add_tx(uid, req):
    """
    Adds a transaction under the User's name. Only adds to the unverified table.
    Request payload should have all necessary parameters.
    
    Args:
        uid (int): The UID of the User to add the transaction to.
    """
    req_body = loads(req.data)
    price = req_body['price']
    motion = req_body['motion']
    description = req_body['description']

    if motion == '':
        motion = 'NULL'
    if description == '':
        description = 'NULL'
        
    tx = Transaction(uid, price, 0, motion=motion, description=description)
    insert('tx_unverified', tx)
    return {'message': f'{tx} added by User {uid}'}