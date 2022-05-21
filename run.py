"""
RUN THIS FILE TO START UP BACKEND SERVER
"""
import os
import argparse

parser = argparse.ArgumentParser()

if __name__ == '__main__':
    args = parser.parse_args()
    # check to make sure database file exists
    if not os.path.exists('resources/drachma.db'):
        # if not, make db and set up file
        exit('DB does not exist -- run setup.py before continuing')