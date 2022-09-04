"""
RUN THIS FILE TO START UP BACKEND SERVER
"""
import os
import argparse

from api import app

parser = argparse.ArgumentParser()
parser.add_argument('--host', default='0.0.0.0', help='host to run backend on')
parser.add_argument('--port', default=4545, help='port to run backend on')

if __name__ == '__main__':
    args = parser.parse_args()
    # check to make sure database file exists
    if not os.path.exists('resources/drachma.db'):
        # if not, make db and set up file
        exit('DB does not exist -- run setup.py before continuing')
        
    app.run(host=args.host, port=args.port, debug=True)