def bad_request_error(msg):
    return {
        'error': f'BAD REQUEST: {msg}'
    }
    
def not_found_error(msg):
    """
    JSON to send on ID not found

    Args:
        msg (string): error message
        
    Returns:
        dict: Error JSON
    """
    return {
        'error': f'ID NOT FOUND: {msg}'
    }