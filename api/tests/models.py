import traceback
from api.models.transaction import Transaction
from api.models.user import User

def test_models():
    try:
        u1 = User('Tester')
        ut1 = Transaction(1, 10, 0, 'Test Motion', 'Unverified by Treasurer')
        vt1 = Transaction(1, 10, 1, 'Test Motion', 'Verified by Treasurer')
    except:
        exit(f'Models test failed:\n{traceback.format_exc()}')