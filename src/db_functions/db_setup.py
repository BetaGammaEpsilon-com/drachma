from src.db_functions.db_operations import run_script

def create_all():
    """
    Creates the all the tables.
    """
    run_script('create_all.sql')
    
def import_drac():
    """
    For importing a .drac file into the database.
    """
    # TODO
    pass