"""
RUN THIS FILE TO SETUP RESOURCES FOR BACKEND
cum - matteo
"""
import os
from api.db_functions import db_setup

DB_NAME = 'drachma.db'
DB_PATH = f'resources/{DB_NAME}'

if __name__ == '__main__':
    # check to see if database file exists
    if os.path.exists(DB_PATH):
        # if it does, reset file
        os.remove(DB_PATH)

    # create all tables
    try:
        db_setup.create_all()
    except Exception as e:
        exit(f'DB setup failed -- check error:\n{e}')
    
    exit(f'DB setup finished successfully')