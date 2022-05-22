def bad_request_error(msg):
    return {
        'error': f'BAD REQUEST: {msg}'
    }