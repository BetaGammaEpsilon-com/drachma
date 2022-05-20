SQL_FOLDER_PATH = 'src/db_functions/sql/'

def run_script(cursor, file):
    """
    Executes a given SQL script. 
    Script must be in the src/db_functions/sql folder

    Args:
        cursor (SQLite Cursor): The cursor to make the query
        file (string): file name
    """
    full_path = SQL_FOLDER_PATH + file
    sql_file = open(full_path, 'r')
    sql = ''.join(sql_file.readlines())
    res = cursor.executescript(sql)

    if res:
        return res