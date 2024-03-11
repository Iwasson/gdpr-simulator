import sqlite3
import time

DB_FILE = 'table.db'
TABLE_NAME = 'new_table'


def create_table(columns):
    """
    Create a new SQLite table with given columns and data types.
    """
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()

    create_query = f"CREATE TABLE {TABLE_NAME} ("
    for column_name, data_type in columns.items():
        create_query += f"{column_name} {data_type}, "
    create_query = create_query[:-2] + ")"  # Remove the last comma and space

    print(create_query)

    c.execute(create_query)

    conn.commit()
    conn.close()

def delete_table_if_exists():
    """
    Delete a table if it exists in an SQLite database.
    """
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()

    c.execute(f"DROP TABLE IF EXISTS {TABLE_NAME}")

    conn.commit()
    conn.close()

def get_table_schema():
    """
    Get the schema of a table in an SQLite database.
    """
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()

    c.execute(f"PRAGMA table_info({TABLE_NAME})")
    schema = c.fetchall()

    conn.close()

    return schema

def insert_data(values):
    """
    Insert data into a table with multiple columns in an SQLite database.
    """
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()

    insert_statement = f"INSERT INTO {TABLE_NAME} VALUES {values};"

    c.execute(insert_statement)

    conn.commit()
    conn.close()

def get_first_n_rows(rows):
    """
    Get the first n rows from a table in an SQLite database.
    """
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()

    select_statement = f"SELECT * FROM {TABLE_NAME} LIMIT {rows};"

    c.execute(select_statement)
    rows = c.fetchall()

    conn.close()

    return rows

def remove_links(link):
    """
    Removes all rows that contain the link value
    """
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute(f"DELETE FROM {TABLE_NAME} WHERE Link={link}")
    conn.commit()
    conn.close()

def get_link_data(link):
    """
    Gets all of the link data
    """
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute(f"SELECT * FROM {TABLE_NAME} WHERE Link={link}")
    conn.commit()

    rows = c.fetchall()
    conn.close()

    return rows

def explain_delete_command(link):
    """
    Runs the SQL Explain command
    """
    explain = []
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute(f'EXPLAIN DELETE FROM {TABLE_NAME} WHERE Link={link}')
        
        explanation = cursor.fetchall()
        for row in explanation:
            explain.append(row)
        
        cursor.close()
        conn.close()

    except sqlite3.Error as e:
        print("SQLite error:", e)
    
    return explain

def delete_transactions(link, num):
    """
    Runs a delete transaction num times
    """
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    conn.execute('BEGIN TRANSACTION')

    times = []
    for _ in range(0, num):
        start_time = time.time()
        cursor.execute(f"DELETE FROM {TABLE_NAME} WHERE Link={link}")
        conn.rollback()
        end_time = time.time()
        times.append(end_time - start_time)

    conn.commit()
    cursor.close()
    conn.close()

    return times
