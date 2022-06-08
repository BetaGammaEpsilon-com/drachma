from api.models import *
from api.db_functions.db_operations import select, sum_col
from api.util.model_factory import *

def get_user_by_uid(uid):
    """
    Given a UID, return the full User

    Args:
        uid (int): The UID to lookup
        
    Returns:
        User: The User accessed at this UID
    """    
    where = f'uid = {uid}'
    result = select('users', where=where)
    if len(result) == 0:
        raise IndexError('No User with that UID in the users table')
    user = create_user_from_sqlresponse(result[0])
    return user

def get_uid_by_name(name):
    """
    Given a User's name, returns the UID of that User

    Args:
        name (string): The name of the User
    """
    columns = ['uid']
    where = f"name = '{name}'"
    result = select('users', where=where, cols=columns)
    if len(result) == 0:
        raise IndexError('No User with that name in the users table')
    uid = result[0][0]
    return uid

def get_transactions_by_uid(uid):
    """
    Gets a list of all Transactions by a certain User

    Args:
        uid (int): The UID of the User

    Returns:
        dict: Two lists of Transactions, verified and unverified
    """
    where = f'uid = {uid}'
    verified = select('tx', where=where)
    unverified = select('tx_unverified', where=where)
    
    # convert to Transaction objects
    if len(verified) != 0:
        verified = [create_tx_from_sqlresponse(sqlrow, 1).serialize() for sqlrow in verified]
    if len(unverified) != 0:
        unverified = [create_tx_from_sqlresponse(sqlrow, 0).serialize() for sqlrow in unverified]
    
    return {
        'verified': verified,
        'unverified': unverified
    }

def get_tx_by_txid(txid):
    """
    Gets a serialized Transaction from whatever table has it

    Args:
        txid (int): The TXID of the transaction

    Returns:
        dict: serialized Transaction
    """
    where = f'txid = {txid}'
    verified = select('tx', where=where)
    unverified = select('tx_unverified', where=where)
    print(verified, unverified)
    
    # convert to Transaction objects
    if len(verified) > 0:
        tx = [create_tx_from_sqlresponse(sqlrow, 1) for sqlrow in verified][0]
    elif len(unverified) > 0:
        tx = [create_tx_from_sqlresponse(sqlrow, 0) for sqlrow in unverified][0]
    else:
        raise IndexError
    return tx

def get_txs():
    """
    Grabs the full list of Transactions from verified/unverified tables

    Returns:
        list: Verified Transactions
        list: Unverified Transactions
    """    
    vres = select('tx')
    ures = select('tx_unverified')
    
    verified = [create_tx_from_sqlresponse(tup, 1).serialize() for tup in vres]
    unverified = [create_tx_from_sqlresponse(tup, 0).serialize() for tup in ures]
    
    return verified, unverified

def get_totals():
    """
    Calculates totals for each table.

    Returns:
        int: Total from Verified table
        int: Total from Unverified table
        int: Total from both tables
    """
    verified_total = sum_col('tx', 'price')[0]
    if verified_total is None:
        verified_total = 0.0
    unverified_total = sum_col('tx_unverified', 'price')[0]
    if unverified_total is None:
        unverified_total = 0.0
    total = verified_total + unverified_total
    
    return verified_total, unverified_total, total

def user_exists(uid):
    """
    Determines whether a User exists in the users table

    Args:
        uid (int): UID of the User to check

    Returns:
        boolean: Whether or not the User exists in the users table
    """
    where = f"uid = {uid}"
    res = select('users', where=where)
    return len(res) > 0

def tx_exists(txid):
    """
    Determines whether a Transaction at given TXID exists

    Args:
        txid (int): The Transaction's TXID

    Returns:
        boolean: Whether or not the Transaction exists
    """
    where = f'txid = {txid}'
    res = select('tx', where=where) + select('tx_unverified', where=where)
    return len(res) > 0

def motion_exists(motion_name):
    """
    Determines whether a motion exists in the motions table

    Args:
        motion_name (str): name of the motion to check

    Returns:
        boolean: Whether or not the motion exists in the motions table
    """
    where = f"motion='{motion_name}'"
    res = select('motions', where=where)
    return len(res) > 0