from datetime import datetime
from dateutil import parser

from api.models.user import User
from api.models.transaction import Transaction

def create_user_from_sqlresponse(sqlres):
    """
    Converts given row of User data into a User object

    Args:
        sqlres (tuple): User entry from users table
        
    Returns:
        User: the User described in this SQL response tuple
    """    
    uid = int(sqlres[0])
    name = sqlres[1]
    balance = float(sqlres[2])
    return User(name, uid=uid, balance=balance)

def create_tx_from_sqlresponse(sqlres, status):
    """
    Converts given row of Transaction data into a Transaction object

    Args:
        sqlres (tuple): Transaction entry from tx or tx_unverified table
        
    Returns:
        Transaction: the Transaction described in this SQL response tuple
    """
    print(sqlres)
    txid = int(sqlres[0])
    uid = int(sqlres[1])
    tx_date = parser.parse(sqlres[2])
    price = float(sqlres[3])
    motion = sqlres[4]
    desc = sqlres[5]
    return Transaction(
        uid, 
        price, 
        status, 
        txid=txid, 
        tx_date=tx_date,
        motion=motion,
        description=desc
    )