def bad_request_error(msg):
    """
    JSON to send when a bad request is made.

    Args:
        msg (dict): error message

    Returns:
        dict: Error JSON
    """
    return {
        'error': f'BAD REQUEST: {msg}'
    }
    
def not_found_error(msg):
    """
    JSON to send on ID not found

    Args:
        msg (str): error message
        
    Returns:
        dict: Error JSON
    """
    return {
        'error': f'ID NOT FOUND: {msg}'
    }

def generic_error(msg):
    """
    JSON to format any error.

    Args:
        msg (str): error message

    Returns:
        dict: Error JSON
    """
    return {
        'error': {msg}
    }