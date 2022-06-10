from datetime import datetime, timedelta
import random

from api.models.transaction import Transaction
from api.logic.visualize import logic_visualize_transaction
from api.logic.transaction import verify_tx
from api.logic.select import get_txs
from api.db_functions.db_operations import insert, select
from api.util.model_factory import create_tx_from_sqlresponse

def test_visualize():
    # make_dummy_tx()s
    v_tx, u_tx = get_txs()
    logic_visualize_transaction(v_tx, u_tx)

def make_dummy_tx():
    today = datetime.today()
    for d in range(0, 31):
        date_to_use = today - timedelta(days=d)
        utx = Transaction(1, random.randrange(10, 100), 0, tx_date=date_to_use, motion='eboard', description='unverified_dummy')
        vtx = Transaction(1, random.randrange(10, 100), 0, tx_date=date_to_use, motion='eboard', description='verified_dummy')
        _test_add_tx(utx)
        _test_add_tx(vtx, verify=True)

def _test_add_tx(tx, verify=False):
    insert('tx_unverified', tx)
    if verify:
        _tx = select('tx_unverified')[-1]
        txid = create_tx_from_sqlresponse(_tx, 0).txid
        verify_tx(txid)