```python
import sqlite3
from sqlite3 import Error

def create_connection():
    conn = None;
    try:
        conn = sqlite3.connect(':memory:') # create a database in RAM
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()

def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def main():
    database = r"C:\sqlite\db\chat2codebot.db"

    sql_create_tasks_table = """ CREATE TABLE IF NOT EXISTS tasks (
                                        id integer PRIMARY KEY,
                                        name text NOT NULL,
                                        priority integer,
                                        status text NOT NULL,
                                        created_at text NOT NULL
                                    ); """

    sql_create_chat_history_table = """CREATE TABLE IF NOT EXISTS chat_history (
                                    id integer PRIMARY KEY,
                                    user_input text NOT NULL,
                                    bot_response text NOT NULL,
                                    timestamp text NOT NULL
                                );"""

    sql_create_user_preferences_table = """CREATE TABLE IF NOT EXISTS user_preferences (
                                    id integer PRIMARY KEY,
                                    preference_name text NOT NULL,
                                    preference_value text NOT NULL
                                );"""

    conn = create_connection(database)

    if conn is not None:
        create_table(conn, sql_create_tasks_table)
        create_table(conn, sql_create_chat_history_table)
        create_table(conn, sql_create_user_preferences_table)
    else:
        print("Error! cannot create the database connection.")

if __name__ == '__main__':
    main()
```