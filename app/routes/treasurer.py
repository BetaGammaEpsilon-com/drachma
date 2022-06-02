from flask import Blueprint, request

from app.logic.select import tx_exists
from app.logic.treasurer import logic_tres_get_all, logic_tres_get_report
from app.util.response import format_json
from app.util.error import not_found_error

URL_PREFIX = '/tres'
tres_bp = Blueprint('tres', __name__, url_prefix=URL_PREFIX)

@tres_bp.route('')
def route_tres():  
    """
    Returns all transactions, separated by verification.
    Metrics like table totals, user totals

    Returns:
        Response: Response to send back
    """
    return format_json(logic_tres_get_all())

@tres_bp.route('/visualize')
def route_visualize():
    """
    

    Returns:
        Response: Response to send back
    """
    return ''

@tres_bp.route('/report')
def route_report():
    """
    

    Returns:
        Response: Response to send back
    """
    return logic_tres_get_report()

@tres_bp.route('/tx', methods=['POST'])
def route_add_tx():
    """
    

    Returns:
        Response: Response to send back
    """
    return ''

@tres_bp.route('/tx/<int:txid>', methods=['GET', 'PUT', 'DELETE'])
def route_update_tx(txid):
    """
    On `GET`: returns information about Transaction txid
    On `PUT`: updates Transaction to have given values
    On `DELETE`: deletes Transaction

    Args:
        txid (int): Transaction txid in database
        
    Returns:
        Response: Response to send back
    """
    if not tx_exists(txid):
        return format_json(not_found_error(f'TXID {txid}'), status=404)
    
    if request.method == 'GET':
        # get Transaction info
        res = ''
    
    elif request.method == 'PUT':
        # update Transaction
        res = ''
    
    elif request.method == 'DELETE':
        # delete Transaction
        res = ''
        
    return format_json(res)