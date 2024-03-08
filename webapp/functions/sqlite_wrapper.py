import sqlite3

DB_FILE = 'table.db'


def create_table(columns, table_name='new_table'):
    """
    Create a new SQLite table with given columns and data types.
    """
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()

    # Construct the CREATE TABLE query
    create_query = f"CREATE TABLE {table_name} ("
    for column_name, data_type in columns.items():
        create_query += f"{column_name} {data_type}, "
    create_query = create_query[:-2] + ")"  # Remove the last comma and space

    print(create_query)

    # Execute the CREATE TABLE query
    c.execute(create_query)

    # Commit and close the connection
    conn.commit()
    conn.close()

def delete_table_if_exists(table_name):
    """
    Delete a table if it exists in an SQLite database.
    """
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()

    # Execute DROP TABLE IF EXISTS statement
    c.execute(f"DROP TABLE IF EXISTS {table_name}")

    # Commit the transaction and close the connection
    conn.commit()
    conn.close()

def get_table_schema(table_name):
    """
    Get the schema of a table in an SQLite database.
    """
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()

    # Execute PRAGMA table_info() to get column information
    c.execute(f"PRAGMA table_info({table_name})")
    schema = c.fetchall()

    # Close the connection
    conn.close()

    return schema

def insert_data(table_name, values):
    """
    Insert data into a table with multiple columns in an SQLite database.
    """
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()

    # Construct the SQL insert statement
    insert_statement = f"INSERT INTO {table_name} VALUES {values};"

    # Execute the insert statement
    c.execute(insert_statement)

    # Commit the transaction and close the connection
    conn.commit()
    conn.close()

def get_first_n_rows(table_name, rows):
    """
    Get the first n rows from a table in an SQLite database.
    """
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()

    # Construct the SQL select statement with LIMIT 20
    select_statement = f"SELECT * FROM {table_name} LIMIT {rows};"

    # Execute the select statement and fetch the results
    c.execute(select_statement)
    rows = c.fetchall()

    # Close the connection
    conn.close()

    return rows
