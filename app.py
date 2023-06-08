import sqlite3
from sqlite3 import Error
import time

def create_connection():
    conn = None;
    try:
        conn = sqlite3.connect('lean_management_quiz.db') # create a database connection
        return conn
    except Error as e:
        print(e)

def create_table(conn, create_table_sql):
    try:
        c = conn.cursor() # create a Cursor object and call its execute() method to perform SQL commands
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def main():
    database = r"lean_management_quiz.db"

    sql_create_profiles_table = """CREATE TABLE IF NOT EXISTS profiles (
                                        id integer PRIMARY KEY,
                                        name text NOT NULL,
                                        created_at text NOT NULL
                                    );"""

    sql_create_results_table = """CREATE TABLE IF NOT EXISTS results (
                                    id integer PRIMARY KEY,
                                    profile_id integer NOT NULL,
                                    category text NOT NULL,
                                    answers text NOT NULL,
                                    created_at text NOT NULL,
                                    FOREIGN KEY (profile_id) REFERENCES profiles (id)
                                );"""
    # create a database connection
    conn = create_connection()

    # create tables
    if conn is not None:
        # create profiles table
        create_table(conn, sql_create_profiles_table)

        # create results table
        create_table(conn, sql_create_results_table)
    else:
        print("Error! cannot create the database connection.")

if __name__ == '__main__':
    main()
