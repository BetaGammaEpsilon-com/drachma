from flask.json import loads

from api.logic.select import get_uid_by_name, get_user_by_uid, get_transactions_by_uid, user_exists
from api.logic.transaction import logic_add_tx, verify_tx
from api.models.transaction import Transaction
from api.models.user import User
from api.db_functions.db_operations import delete, insert, select, update
from api.util.model_factory import create_user_from_sqlresponse, create_tx_from_sqlresponse

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

def logic_create_user(req):
    """
    Creates a new User in the `users` table.

    Args:
        req (Flask.Request): The request from the frontend.
    """
    req_body = loads(req.data)
    name = req_body['name']
    balance = req_body['balance']

    new_user = User(name, balance=balance)

    insert('users', new_user)
    uid = get_uid_by_name(name)

    # create a Transaction to balance book
    if balance != 0:
        tx = Transaction(uid, balance, 0, motion='eboard', description=f'Balance of new User: {name}')
        logic_add_tx()
        last_tx = select('tx_unverified')[-1]
        txid = create_tx_from_sqlresponse(last_tx, 0).txid
        verify_tx(txid)

    return {'message': f'New user created successfully.'}

def logic_delete_user(uid):
    """
    Deletes the User at UID

    Args:
        uid (int): The User ID
    """
    if not user_exists(uid):
        raise IndexError(f'User {uid} not found')
    
    delete('users', where=f'uid={uid}')
    return {'message': f'Successfully deleted User {uid}'}

def logic_get_users(serialize=True):
    """
    Grabs the list of all Users in the 

    Returns:
        list: List of serialized Users
    """    
    res = select('users')
    if serialize:
        return [create_user_from_sqlresponse(tup).serialize() for tup in res]
    else:
        return [create_user_from_sqlresponse(tup) for tup in res]

def update_balance(uid):
    """
    Updates the balance of a user by scanning through the verified transactions and totals them for the given User.

    Args:
        uid (int): The User ID of the User whose balance gets updated
    """
    # get all verified transactions
    verified = get_transactions_by_uid(uid)['verified']
    
    # sum totals
    balance = sum([t['price'] for t in verified])
    
    # update balance in users table
    set_sql = f'balance = {balance}'
    where = f'uid = {uid}'
    update('users', set_sql, where)
    print(f'Updated balance of User {uid} to {balance}')