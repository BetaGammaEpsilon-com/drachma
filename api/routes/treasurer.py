from flask import Blueprint, request

from api.logic.select import tx_exists
from api.logic.treasurer import logic_tres_delete_tx, logic_tres_get_all, logic_tres_get_report, logic_tres_get_tx, logic_tres_modify_tx
from api.logic.motions import logic_motions_get_all, logic_motions_create_motion, logic_motions_delete_motion
from api.logic.transaction import logic_add_tx

from api.util.response import format_json
from api.util.error import generic_error, not_found_error, bad_request_error

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
    return format_json(logic_tres_get_report())

@tres_bp.route('/tx', methods=['POST'])
def route_add_tx():
    """
    Adds a Transaction to the Unverfied table, then immediately verifies it.

    Returns:
        Response: Response to send back
    """
    try:
        return format_json(logic_add_tx(request, verified=True))
    except KeyError:
        return format_json(bad_request_error(f'Request to add a Transaction must include valid `uid`, `price`, `motion`, and `description` fields.'), status=400)
    except RuntimeError:
        return format_json(not_found_error(f'Motion specified does not exist.'), status=404)

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
        res = logic_tres_get_tx(txid)
    
    elif request.method == 'PUT':
        # update Transaction
        try:
            res = logic_tres_modify_tx(txid, request)
        except IndexError:
            return format_json(not_found_error(f'Cannot update Transaction: motion does not exist'), status=404)
    
    elif request.method == 'DELETE':
        # delete Transaction
        res = logic_tres_delete_tx(txid)
        
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
        except RuntimeError:
            return format_json(bad_request_error('Motion name must be unique.'), status=401)
        except:
            return format_json(generic_error('Unknown error in POST to /tres/motions'), status=500)
    
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
