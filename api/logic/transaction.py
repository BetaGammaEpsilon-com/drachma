from flask.json import loads

from api.logic.select import motion_exists
from api.models.transaction import Transaction
from api.db_functions.db_operations import insert

def logic_add_tx(req, uid=None):
    """
    Adds a Transaction and adds it to the Unverified Table

    Args:
        req (dict): The Request
        uid (int, optional): The User ID owner of this transaction
    """
    req_body = loads(req.data)
    price = req_body['price']
    motion = req_body['motion']
    description = req_body['description']

    if not uid:
        uid = req_body['uid']

    if description == '':
        description = 'NULL'

    if not motion_exists(motion):
        raise RuntimeError
        
    tx = Transaction(uid, price, 0, motion=motion, description=description)
    insert('tx_unverified', tx)
    return {'message': f'{tx} added by User {uid}'}
    