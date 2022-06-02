from app.db_functions.db_operations import select, run_script, sum_col
from app.util.model_factory import create_tx_from_sqlresponse, create_user_from_sqlresponse

def logic_tres_get_all():
    """
    Returns all transactions, separated by verification.
    Metrics like table totals, user totals

    Returns:
        Response: Response to send back
    """
    v_tx, u_tx = _get_tx()
    v_tot, u_tot, tot = _get_totals()
    users = [u.serialize() for u in _get_users()]
    return {
        'verified_tx': v_tx,
        'unverified_tx': u_tx,
        'verified_total': v_tot,
        'unverified_total': u_tot,
        'total': tot,
        'users': users
    }
    
def _get_tx():
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

def _get_users():
    """
    Grabs the list of all Users in the 

    Returns:
        list: List of serialized Users
    """    
    res = select('users')
    return [create_user_from_sqlresponse(tup) for tup in res]

def _get_totals():
    """
    Calculates totals for each table.

    Returns:
        int: Total from Verified table
        int: Total from Unverified table
        int: Total from both tables
    """
    verified_total = sum_col('tx', 'price')[0]
    unverified_total = sum_col('tx_unverified', 'price')[0]
    total = verified_total + unverified_total
    
    return verified_total, unverified_total, total

def logic_tres_get_report():
    """
    Pulls users from database and generates markdown string to be displayed by the frontend
    Return:
        dict: type = report and report = formatted markdown string to create table
    """
    users = _get_users()
    report = f"| Brother | Balance |\n| :--- | :---: |\n"
    for u in users:
        report += u.markdownify() + '\n'
    print(report)
    return {
        'type': 'report',
        'report': report
    }