import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    """create a database connection to SQLite database
    :param db_file: database file
    return: Connection"""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    return conn


def create_table(conn, create_table_sql):
    """create a table from the create_table_sql statement
    :param conn: Connection obj
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def create_user(conn, user):
    """Create new user
    :param conn:
    :param user:
    :return: uid"""
    sql =   ''' INSERT INTO users(uid, name)
                VALUES(?,?)'''
    c = conn.cursor()
    c.execute(sql, user)
    conn.commit()

    return c.lastrowid

def create_tx(conn, tx):
    """Create new tx
    :param conn:
    :param tx:
    :return: uid"""
    sql =   ''' INSERT INTO(id, tx_date, price, status, desc)
                VALUES(?,?,?,?,?)'''
    c = conn.cursor()
    c.execute(sql, tx)
    conn.commit()

    return c.lastrowid

def update_user(conn, user):
    """Update a user
    :param conn:
    :param user:
    :return: uid"""
    sql =   ''' UPDATE users
                SET name = ?
                WHERE uid = ?'''
    c = conn.cursor()
    c.execute(sql, user)
    conn.commit()

def update_tx(conn, tx):
    """Update a transaction
    :param conn:
    :param tx:
    :return: id"""
    sql = ''' UPDATE tx
                    SET tx_date = ?
                    price = ?
                    status = ?
                    WHERE id = ?'''
    c = conn.cursor()
    c.execute(sql, tx)
    conn.commit()

def delete_user(conn, user):
    """Delete a user
    :param conn:
    :param user:
    :return: uid"""
    sql = 'DELETE FROM users WHERE uid=?'
    c = conn.cursor()
    c.execute(sql, user)
    conn.commit()

def delete_tx(conn, tx):
    """Delete a tx
    :param conn:
    :param tx:
    :return: id"""
    sql = 'DELETE FROM tx WHERE id=?'
    c = conn.cursor()
    c.execute(sql, tx)
    conn.commit()

if __name__ == '__main__':
    db = r"C:\Users\joshg\PycharmProjects\drachma\drach.db"
    sql_create_users_table =    """ CREATE TABLE IF NOT EXISTS users (
                                    uid integer PRIMARY KEY,
                                    name text NOT NULL
                                ); """
    sql_create_tx_table =   """ CREATE TABLE IF NOT EXISTS tx (
                                tx_id integer PRIMARY KEY,
                                uid integer NOT NULL
                                tx_date date NOT NULL,
                                price float NOT NULL,
                                status tinyint NOT NULL,
                                desc text
                            ); """

    conn = create_connection(db)

    if conn is not None:
        create_table(conn, sql_create_users_table)
        create_table(conn, sql_create_tx_table)
    else:
        print("ERROR: cannot create connection")