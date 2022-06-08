import sqlite3

SQL_FOLDER = 'api/db_functions/sql/'
DATABASE_PATH = 'resources/drachma.db'

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
    
def select(tbl, where=None, cols=[]):
    """
    Selects from table where condition is met.

    Args:
        tbl (string): Table name of table to select from
        where (string): The SQL containing the WHERE condition
        cols (list, optional): Columns to pull from query. 
            If no columns are specified it will pull whole table.
            
    Returns:
        list: rows returned from SELECT
    """
    conn = create_connection()
    cursor = conn.cursor()
    if len(cols) > 0:
        sql = f'''
            SELECT ({', '.join(cols)}) FROM 
                {tbl}'''
    else:
        sql = f'''
            SELECT * FROM 
                {tbl}'''
    
    if where:
        sql += f' WHERE {where};'
    # print(sql)
    cursor.execute(sql)
    res = cursor.fetchall()
    conn.close()
    
    return res

def run_script(file):
    """
    Executes a given SQL script. 
    Script must be in the app/db_functions/sql folder

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

def sum_col(tbl, col):
    """
    Sums a column in the given table

    Args:
        tbl (string): Name of the table
        col (string): Column to sum

    Returns:
        int: sum
    """
    conn = create_connection()
    cursor = conn.cursor()
    
    sql = f'SELECT SUM({col}) FROM {tbl};'
    
    cursor.execute(sql)
    res = cursor.fetchone()
    conn.close()
    if len(res) == 0:
        res = 0
    return res

def insert_motion(motion):
    """
    Inserts into the motions table

    Args:
        motion (str): the new motion
    """
    conn = create_connection()
    cursor = conn.cursor()
    
    sql = f"INSERT INTO motions VALUES ('{motion}', CURRENT_TIMESTAMP);"

    cursor.execute(sql)
    conn.close()