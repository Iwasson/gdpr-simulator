import random
import string


def generate_rand_string(length: int) -> str:
    letters = string.ascii_letters
    return "".join(random.choice(letters) for _ in range(length))

def generate_rand_num(length: int) -> int:        
    min_value = 10 ** (length - 1)
    max_value = (10 ** length) - 1
    return random.randint(min_value, max_value)

def generate_rand_float(length: int) -> float:        
    min_value = 10 ** (length - 1)
    max_value = (10 ** length) - 1
    return random.uniform(min_value, max_value)

def generate_schema(num_cols: int) -> list[str]:
    """
    Takes in the number of columns present in the desired DB schema
    and returns a list of all of the columns and their data types
    generated at random.
    """
    col_types = [
        "INTEGER",
        "REAL",
        "TEXT",
    ]

    schema = {
        "Link": "INTEGER",
    }

    for num in range(0, num_cols):
        col_name = f"{generate_rand_string(10)}"
        col = {col_name: col_types[random.randint(0, len(col_types) - 1)]}
        schema.update(col)

    return schema
