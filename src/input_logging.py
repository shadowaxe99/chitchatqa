```python
import sqlite3
from sqlite3 import Error

def create_connection():
    conn = None;
    try:
        conn = sqlite3.connect('chatbot_database.db') # Create a database connection to a SQLite database
        return conn
    except Error as e:
        print(e)

    return conn

def log_input(conn, user_input, bot_response):
    try:
        cursor = conn.cursor()
        query = ''' INSERT INTO interactions(user_input,bot_response)
                    VALUES(?,?) '''
        cursor.execute(query, (user_input, bot_response))
        conn.commit()
    except Error as e:
        print(e)

def get_all_interactions(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM interactions")

    rows = cursor.fetchall()

    for row in rows:
        print(row)

def main():
    database = r"chatbot_database.db"

    sql_create_interactions_table = """ CREATE TABLE IF NOT EXISTS interactions (
                                        id integer PRIMARY KEY,
                                        user_input text NOT NULL,
                                        bot_response text
                                    ); """

    conn = create_connection()

    if conn is not None:
        create_table(conn, sql_create_interactions_table)
    else:
        print("Error! cannot create the database connection.")

if __name__ == '__main__':
    main()
```