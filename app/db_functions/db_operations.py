import sqlite3

SQL_FOLDER = 'src/db_functions/sql/'
DATABASE_PATH = 'resources/drachma.db'

def run_script(file):
    """
    Executes a given SQL script. 
    Script must be in the src/db_functions/sql folder

    Args:
        cursor (SQLite Cursor): The cursor to make the query
        file (string): file name
    """
    conn = create_connection()
    cursor = conn.cursor()
    
    full_path = SQL_FOLDER + file
    sql_file = open(full_path, 'r')
    sql = ''.join(sql_file.readlines())
    
    res = cursor.executescript(sql)
    conn.commit()
    conn.close()
    return res

def create_connection():
    """
    Create a database connection to SQLite database

    Returns:
        SQLite Connection: the connection object
    """
    try:
        conn = sqlite3.connect(DATABASE_PATH)
    except Exception as e:
        raise RuntimeError(f'Error connecting to database file {DATABASE_PATH}: {e}')
    return conn

def table_exists(conn, tbl):
    """
    Checks whether table `tbl` exists in the database.

    Args:
        conn (SQLite Connection): The connection
        tbl (string): The name of the table to check
    """
    cursor = conn.cursor()
    cursor.execute('''
        SELECT 
            name
        FROM 
            sqlite_master
        WHERE 
            type = 'table';
    ''')
    res = cursor.fetchall()
    # extracts table names
    tables = [t[0] for t in res]
    return tbl in tables

def insert(tbl, entry):
    """
    Inserts given Entry into given table.

    Args:
        tbl (string): The table to insert into
        entry (Model): The row entry to insert
    """
    conn = create_connection()
    
    if not table_exists(conn, tbl):
        raise RuntimeError(f'Error while inserting {entry}:\nTable {tbl} does not exist.')

    if tbl != entry.tbl:
        raise RuntimeError(f'Error while inserting {entry}:\nCannot insert {entry} into {tbl}.')

    cursor = conn.cursor()
    
    columns, values = entry.sqlify()
    
    insert_sql = f'INSERT INTO {tbl}({columns}) VALUES ({values});'

    cursor.execute(insert_sql)
    conn.commit()
    conn.close()
    
def update(tbl, set, where):
    """
    Updates given table according to the script condition.

    Args:
        tbl (string): Table name of table to be updated
        set (string): The SQL containing the SET condition
        where (string): The SQL containing the WHERE condition
    """
    conn = create_connection()
    cursor = conn.cursor()
    sql = f'''
        UPDATE 
            {tbl}
        SET
            {set}
        WHERE
            {where};
    '''
    cursor.execute(sql)
    conn.commit()
    conn.close()
    
def delete(tbl, where):
    """
    Deletes from given table where condition is met.

    Args:
        tbl (string): Table name of table to be updated
        where (string): The SQL containing the WHERE condition
    """    
    conn = create_connection()
    cursor = conn.cursor()
    sql = f'''
        DELETE FROM 
            {tbl}
        WHERE
            {where};
    '''
    cursor.execute(sql)
    conn.commit()
    conn.close()