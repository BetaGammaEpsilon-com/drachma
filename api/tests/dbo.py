import traceback
import uuid

from api.db_functions.db_operations import *
from api.models.transaction import Transaction
from api.models.user import User

def test_dbo():
    conn = create_connection()
    
    # all tests go in try block
    try:
        # table_exists tests
        assert table_exists(conn, 'tx')
        assert table_exists(conn, 'users')
        assert not table_exists(conn, 'failure')
        
        # attempt to insert
        u1 = User(uuid.uuid4())
        ut1 = Transaction(1, 10, 0, 'Test Motion', 'Unverified by Treasurer')
        
        insert('users', u1)
        insert('tx_unverified', ut1)
    
    except:
        exit(f'DBO test failed:\n{traceback.format_exc()}')
        
    conn.close()