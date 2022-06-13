from flask.json import loads

from api.db_functions.db_operations import update, delete
from api.logic.user import logic_get_users, update_balance
from api.logic.select import get_txs, get_totals, get_tx_by_txid, motion_exists, get_user_by_uid
from api.logic.transaction import verify_tx
from api.models.txstatus import TxStatus

def logic_tres_get_all():
    """
    Returns all transactions, separated by verification.
    Metrics like table totals, user totals

    Returns:
        Response: Response to send back
    """
    v_tx, u_tx = get_txs()
    v_tot, u_tot, tot = get_totals()
    users = [u for u in logic_get_users()]

    paired_vtx = []
    for tx in v_tx:
        uid = tx['uid']
        user = get_user_by_uid(uid).serialize()
        paired_vtx.append({
            'transaction': tx,
            'user': user
        })

    paired_utx = []
    for tx in u_tx:
        uid = tx['uid']
        user = get_user_by_uid(uid).serialize()
        paired_utx.append({
            'transaction': tx,
            'user': user
        })

    return {
        'verified_tx': paired_vtx,
        'unverified_tx': paired_utx,
        'verified_total': v_tot,
        'unverified_total': u_tot,
        'total': tot,
        'users': users
    }

def logic_tres_get_report():
    """
    Pulls users from database and generates Markdown string to be displayed by the frontend
    
    Returns:
        dict: type = report and report = formatted Markdown string to create table
    """
    users = logic_get_users(serialize=False)
    report = f'| Brother | Balance |\n| :--- | :---: |\n'
    
    for u in users:
        report += u.markdownify() + '\n'

    return {
        'type': 'report',
        'report': report
    }
    
def logic_tres_get_tx(txid):
    """
    Gets the Transaction associated with the TXID given.

    Args:
        txid (int): The TXID of the Transaction to look up

    Returns:
        dict: The unserialized Response
    """    
    tx = get_tx_by_txid(txid)
    return {
        'transaction': tx.serialize(),
        'user': get_user_by_uid(tx.uid).serialize()
    }

def logic_tres_modify_tx(txid, req):
    """
    For modifying a Transaction, including verification.

    Args:
        txid (int): The Transaction ID
        req (flask.Request): The Request object

    Raises:
        IndexError: If the motion supplied does not exist

    Returns:
        dict: Response message
    """
    change_date = False
    tx = get_tx_by_txid(txid)
    pre_status = tx.status
    tx = tx.serialize()
    req_body = loads(req.data)

    # grab vars from request
    uid = req_body['uid']
    price = req_body['price']
    motion = req_body['motion']
    description = req_body['description']
    status = req_body['status']

    if not motion_exists(motion):
        raise IndexError

    # if anything changes, update tx_date
    if tx['uid'] != uid or tx['price'] != price or tx['motion'] != motion or tx['description'] != description:
        change_date = True

    # make update
    table = 'tx' if pre_status == 1 else 'tx_unverified'
    if change_date:
        set_sql = f"uid={uid}, tx_date=CURRENT_TIMESTAMP, price={price}, motion='{motion}', description='{description}'"
    else:
        set_sql = f"uid={uid}, tx_date='{tx['tx_date']}', price={price}, motion='{motion}', description='{description}'"
    where_sql = f'txid={txid}'
    update(table, set_sql, where_sql)

    # verify transaction
    if pre_status == TxStatus.UNVERIFIED and status == 1:
        verify_tx(txid)

    return {'message': f'Transaction {txid} successfully modified.'}

def logic_tres_delete_tx(txid):
    """
    Deletes a Transaction at the given TXID.

    Args:
        txid (int): The Transaction TXID

    Returns:
        dict: Response
    """
    tx = get_tx_by_txid(txid)
    delete('tx_unverified', f'txid={txid}')
    delete('tx', f'txid={txid}')
    update_balance(tx.uid)
    
    return {'message': f'Transaction {txid} successfully deleted.'}
