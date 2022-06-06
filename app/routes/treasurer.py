from flask import Blueprint, request

from app.logic.select import motion_exists, tx_exists
from app.logic.treasurer import logic_tres_get_all, logic_tres_get_report
from app.logic.motions import logic_motions_get_all, logic_motions_create_motion, logic_motions_delete_motion
from app.util.response import format_json
from app.util.error import generic_error, not_found_error, bad_request_error

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

@tres_bp.route('/report')
def route_report():
    """
    Return Markdown string to be formatted as a table of users and corresponding balances

    Returns:
        Response: Response to send back
    """
    return logic_tres_get_report()

@tres_bp.route('/tx', methods=['POST'])
def route_add_tx():
    """
    Adds a Transaction to the Unverfied table, then immediately verifies it.

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
    TODO

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

@tres_bp.route('/motions', methods=['GET', 'POST', 'DELETE'])
def route_motions():
    """
    On `GET`: returns all motions
    On `POST`: creates a motion
    On `DELETE`: deletes a motion

    Returns:
        Response: Response to send back
    """
    if request.method == 'GET':
        # get all motions
        res = logic_motions_get_all()
    
    elif request.method == 'POST':
        # create motion
        try:
            res = logic_motions_create_motion(request)
        except KeyError:
            return format_json(bad_request_error('request must include `motion` parameter.'), status=400)
        except:
            return format_json(generic_error('Unknown error in POST to /tres/motions'), status=401)
    
    elif request.method == 'DELETE':
        # delete motion
        try:
            res = logic_motions_delete_motion(request)
        except KeyError:
            return format_json(bad_request_error('request must include `motion` parameter.'), status=400)
        except IndexError:
            return format_json(not_found_error(f'motion not found.'), status=404)

    return format_json(res)

@tres_bp.route('/visualize')
def route_visualize():
    """
    TODO
    Returns:
        Response: Response to send back
    """
    return ''
