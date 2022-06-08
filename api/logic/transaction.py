from flask.json import loads

from api.logic.select import motion_exists
from api.logic.treasurer import verify_tx
from api.models.transaction import Transaction
from api.db_functions.db_operations import insert, select
from api.util.model_factory import create_tx_from_sqlresponse

def logic_add_tx(req, uid=None, verified=False):
    """
    Adds a Transaction and adds it to the database.

    Args:
        req (dict): The Request
        uid (int, optional): The User ID owner of this transaction
        verified (boolean, optional): When False, does not immediately verify the Transaction. When True, Transaction is automatically verified.
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
        raise IndexError
        
    tx = Transaction(uid, price, 0, motion=motion, description=description)
    insert('tx_unverified', tx)

    res = {'message': f'{tx} added by User {uid}'}

    if verified:
        last_tx = select('tx_unverified')[-1]
        txid = create_tx_from_sqlresponse(last_tx, 0).txid
        print('most recent tx ID is', txid)
        verify_tx(txid)
        res = {'message': f'{tx} added by Treasurer'}

    return res
    