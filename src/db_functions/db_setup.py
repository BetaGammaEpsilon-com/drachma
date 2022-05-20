import sqlite3
from src.db_functions.db_query import run_script

def create_all(db_path):
    """
    Creates the main database, then all the tables.
    Database file gets created to db_path

    Args:
        db_path (string): The path to the database file
    """

    # connection
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # run SQL
    run_script(cursor, 'create_all.sql')
    
    # close connection
    conn.close()