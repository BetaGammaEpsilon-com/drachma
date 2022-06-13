from flask.json import loads

from api.db_functions.db_operations import select, insert_motion, delete
from api.logic.select import motion_exists

def logic_motions_get_all():
    """
    Returns all the current motions that exist.

    Returns:
        list: list of dictionary-formatted motions
    """
    motions = select('motions')
    return [_format_motion_from_sqlresponse(m) for m in motions]

def logic_motions_create_motion(req):
    """
    Creates a motion.

    Args:
        req (Flask.Request): The Request object

    Raises:
        RuntimeError: When the motion already exists.

    Returns:
        dict: The success message
    """
    req_body = loads(req.data)
    motion = req_body['motion']
    
    # don't add if motion already exists
    if motion_exists(motion):
        raise RuntimeError('motion already exists')
    
    insert_motion(motion)
    return {'message': f'Motion `{motion}` inserted successfully'}

def logic_motions_delete_motion(req):
    """
    Deletes a motion.

    Args:
        req (flask.Request): The Request object

    Raises:
        IndexError: When the motion requested does not exist.

    Returns:
        dict: Message on successful deletion
    """
    req_body = loads(req.data)
    motion = req_body['motion']

    if not motion_exists(motion):
        raise IndexError(f'motion {motion} does not exist, and cannot be deleted.')

    delete('motions', f"motion='{motion}'")
    return {'message': f'Motion `{motion}` deleted successfully'}

def _format_motion_from_sqlresponse(sql):
    """
    Formats the motion SQL Response into the appropriate packet response.

    Args:
        sql (tuple): The response from the SQL Select

    Returns:
        dict: The formatted Response dict
    """
    return {
        'motion': sql[0],
        'date_added': sql[1]
    }