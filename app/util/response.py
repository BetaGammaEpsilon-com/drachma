from flask import Response
from flask.json import dumps

def format_json(dumpable, status=200):
    """
    Converts JSON-serializable object into Flask Response object.

    Args:
        dumpable (dict): object to send
        code (int): status code
        
    Returns:
        Response: the response
    """
    return Response(dumps(dumpable), status=status, mimetype='application/json')