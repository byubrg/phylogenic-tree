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

def create_tree(conn, tree):
    """
    Create a new task
    :param conn:
    :param tree:
    :return:
    """
    sql = ''' INSERT INTO Tree(Username,Newick_string) VALUES(?,?) '''
    cur = conn.cursor()
    cur.execute(sql, tree)
    return cur.lastrowid

def edit_tree(conn, tree):
    """
    update Newik string of a tree
    :param conn:
    :param tree:
    :return: project id
    """
    sql = ''' UPDATE tasks
              SET Newick_string = ?
              WHERE Username = ?'''
    cur = conn.cursor()
    cur.execute(sql, tree)
    conn.commit()
    
def delete_task_tree(conn, user):
    """
    Delete a task by task id
    :param conn:  Connection to the SQLite database
    :param user: owner of the tree
    :return:
    """
    sql = 'DELETE FROM Tree WHERE user =?'
    cur = conn.cursor()
    cur.execute(sql, (user,))
    conn.commit()
    
def main():
    database = r"C:\Users\Snic9\BRG\SQlite Database Test.db"
    # create a database connection
    conn = create_connection(database)
    with conn:
        user = input("Enter your username")
        stuff = input("What would you like to do? Options: create, edit, and delete")
        if stuff == "create":
            stuff = input("Would you like to enter a Newick string or edit later? Y/N")
            if stuff == "Y":
                tree = input("Enter Newick string")
                create = (user, tree)
                location = create_tree(conn, create)
            else:
                tree = 'Blank'
                create = (user, tree)
                location = create_tree(conn, create)
        elif stuff == "edit":
            tree = input("Enter Newick string")
            edit_tree(conn, (user, tree))
        elif stuff == "delete":
            delete_task_tree(conn, user)
            
if __name__ == "__main__":
    main()
