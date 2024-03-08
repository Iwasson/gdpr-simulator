import random
import numpy as np
from schema_generator import generate_rand_string, generate_rand_num, generate_schema

def generate_numbers(distribution, size=1):
    if distribution == "uniform":
        return [random.randint(0, 100) for _ in range(size)]
    elif distribution == "normal":
        # Using numpy's normal distribution function
        mu = 50  # Mean
        sigma = 20  # Standard deviation
        numbers = np.random.normal(mu, sigma, size)
        return list(np.round(numbers).astype(int))
    elif distribution == "exponential":
        # Using numpy's exponential distribution function
        scale = 50  # Scale parameter (inverse of rate parameter)
        numbers = np.random.exponential(scale, size)
        return list(np.round(numbers).astype(int))

def seed_db(num_rows: int, num_cols: int, linking_strength: float) -> None:
  #schema = generate_schema(num_cols)
    
  return generate_numbers("normal", size=num_rows)

  