from flask.json import loads

from api.db_functions.db_operations import select, insert_motion, delete
from api.logic.select import motion_exists

def logic_motions_get_all():
    motions = select('motions')
    return [_format_motion_from_sqlresponse(m) for m in motions]

def logic_motions_create_motion(req):
    req_body = loads(req.data)
    motion = req_body['motion']
    
    # don't add if motion already exists
    if motion_exists(motion):
        raise RuntimeError
    
    insert_motion(motion)
    return {'message': f'Motion `{motion}` inserted successfully'}

def logic_motions_delete_motion(req):
    req_body = loads(req.data)
    motion = req_body['motion']

    if not motion_exists(motion):
        raise IndexError

    delete('motions', f'motion = {motion}')
    return {'message': f'Motion `{motion}` deleted successfully'}

def _format_motion_from_sqlresponse(sql):
    return {
        'motion': sql[0],
        'date_added': sql[1]
    }