"""
RUN THIS FILE TO START UP BACKEND SERVER
"""
import os

if __name__ == '__main__':
    # check to make sure database file exists
    if not os.path.exists('resources/drachma.db'):
        # if not, make db and set up file
        exit('DB does not exist -- run setup.py before continuing')