import random
import numpy as np

from .analytics import display_histogram
from .schema_generator import generate_rand_string, generate_rand_num, generate_schema, generate_rand_float
from .sqlite_wrapper import create_table, delete_table_if_exists, insert_data


def generate_numbers(distribution, size=1, std=10):
    if distribution == "uniform":
        return [random.randint(0, 100) for _ in range(size)]
    elif distribution == "normal":
        # Using numpy's normal distribution function
        mu = 50  # Mean
        sigma = std  # Standard deviation
        numbers = np.random.normal(mu, sigma, size)
        return list(np.round(numbers).astype(int))
    elif distribution == "exponential":
        # Using numpy's exponential distribution function
        scale = 50  # Scale parameter (inverse of rate parameter)
        numbers = np.random.exponential(scale, size)
        return list(np.round(numbers).astype(int))
    
def generate_rand_data(datatype):
    data = None
    if datatype == "INTEGER":
        data = generate_rand_num(10)
    elif datatype == "REAL":
        data = generate_rand_float(10)
    elif datatype == "TEXT":
        data = generate_rand_string(10)
    return data

def seed_db(num_rows: int, num_cols: int, linking_strength: int) -> dict:
    # get the random columns and their types
    schema = generate_schema(num_cols)

    # get the random linking values, a higher linking strength means more standard deviation
    links = generate_numbers("normal", size=num_rows, std=linking_strength)

    # delete any existing tables if they exist
    delete_table_if_exists()

    # for each key in the schema, insert column into DB
    create_table(schema)

    # log the schema to make sure its working
    #print(get_table_schema(table_name))

    # for each row, generate random data that fits the column type and insert
    for num in range(0, num_rows):
        values = ()
        for key in schema.keys():
            # key stores the name of the column
            # schema[key] stores the datatype
            if key == "Link":
                values = (links[num],) + values
            else:
                values = values + (generate_rand_data(schema[key]),)
        
        insert_data(values)
    
    display_histogram(links)
    return schema, links