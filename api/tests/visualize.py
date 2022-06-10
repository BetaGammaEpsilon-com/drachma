from api.logic.visualize import logic_visualize_transaction
from api.logic.select import get_txs

def test_visualize():
    v_tx, u_tx = get_txs()
    logic_visualize_transaction(v_tx, u_tx)
