import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    return conn

def create_Account(conn, tree):
    """
    Create a new Account
    :param conn:
    :param tree:
    :return:
    """
    sql = ''' INSERT INTO Users(userName, Password) VALUES(?,?) '''
    cur = conn.cursor()
    cur.execute(sql, tree)
    return cur.lastrowid

def edit_password(conn, tree):
    """
    update Password on an account
    :param conn:
    :param tree:
    :return: project id
    """
    sql = ''' UPDATE Users
              SET Password = ?
              WHERE userName = ?'''
    cur = conn.cursor()
    cur.execute(sql, tree)
    conn.commit()
    
def delete_Account(conn, user):
    """
    Delete an account by Username
    :param conn:  Connection to the SQLite database
    :param user: owner of the tree
    :return:
    """
    sql = 'DELETE FROM Users WHERE userName =?'
    cur = conn.cursor()
    cur.execute(sql, (user,))
    conn.commit()
    
def main():
    database = r"C:\Users\Snic9\BRG\SQlite Database Test.db"
    # create a database connection
    conn = create_connection(database)
    with conn:
        user = input("Would you like to sign in or create an account? Options: sign in or create")
        if user == "create":
            name = input("Please input a username")
            key = input("Please input a password")
            tree = (name, key)
            location = create_Account(conn, tree)
        else:
            name = input("Enter your username")
            key = input("Enter your password")
            user = input("Would you like to change your password or delete your account? Options: change or delete")
            if user == "delete":
                delete_Account(conn, name)
            elif user == "change":
                newkey = input("Enter your new password")
                edit_password(conn, (newkey, name))
                
if __name__ == "__main__":
    main()
