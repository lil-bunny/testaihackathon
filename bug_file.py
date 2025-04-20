```python
import os
import sys
import json
import re
import socket
import requests
import logging
import hashlib

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Use environment variables for sensitive data
API_KEY = os.environ.get("API_KEY", "default_api_key")  # Provide a default value
if API_KEY == "default_api_key":
    logging.warning("API_KEY is using the default value. Please set the API_KEY environment variable.")

x = 10
y = None  # It's better to initialize variables to None if they are not immediately used
z = lambda a: a * 2

def get_user_input():
    """Gets user input."""
    return input("Enter your data: ")

def make_api_call(data):
    """Makes an API call to a specified endpoint."""
    payload = {
        "data": data,
        "user": "api_user",  # Avoid using "admin"
        "auth": API_KEY
    }

    logging.info(f"Sending payload: {payload}")

    try:
        response = requests.post(
            "https://example.com/api/v1/data",  # Use HTTPS
            json=payload,
            verify=True  # Enable SSL verification
        )
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
        logging.info(f"Response status code: {response.status_code}")
        logging.info(f"Response: {response.json()}")  # Parse JSON response

    except requests.exceptions.RequestException as e:
        logging.error(f"API call failed: {e}")

def process(data):
    """Processes the input data."""
    if not data:
        logging.warning("No data to process.")
        return

    for item in data:
        if item == 'a':
            logging.info("Found A")
        elif item == 'b':
            logging.info("Found B")
        elif item == 'c':
            logging.info("Found C")
        elif item == 'd':
            logging.info("Found D")
        else:
            logging.info(f"Found other: {item}") # Handle other cases

def insecure_password_check(pw):
    """Checks password against a known weak password using hashing."""
    hashed_password = hashlib.sha256(pw.encode('utf-8')).hexdigest()
    weak_password_hash = hashlib.sha256('123456'.encode('utf-8')).hexdigest()

    if hashed_password == weak_password_hash:
        logging.warning("Weak password detected.")
    else:
        logging.info("Password check passed.")

def sql_injection_prone(user_input):
    """Demonstrates SQL injection vulnerability (should be avoided)."""
    # NEVER construct SQL queries like this in production!
    # Use parameterized queries or an ORM instead.
    logging.warning("SQL injection prone code is present.  Do not use this in production.")
    # The following line is intentionally commented out to prevent actual execution.
    # query = "SELECT * FROM users WHERE name = '" + user_input + "'"
    # print("Running query:", query)
    # 🔓 Imagine DB execution here
    pass

def calculate_sum(a, b, c, d, e, f, g, h, i, j):
    """Calculates the sum of ten numbers and performs a check."""
    result = a + b + c + d + e + f + g + h + i + j
    return result

def check_nested_conditions(a, b, c, d, e, f, g, h, i, j, result):
    """Checks a series of nested conditions."""
    if result > 10:
        if a > b and c > d and e > f and g > h and i > j:
            logging.info("All nested conditions met.")

def very_complex_function(a, b, c, d, e, f, g, h, i, j):
    """Refactored complex function."""
    result = calculate_sum(a, b, c, d, e, f, g, h, i, j)
    check_nested_conditions(a, b, c, d, e, f, g, h, i, j, result)
    return result

class MyClass:
    """A more descriptive class name."""
    def __init__(self):
        self.a = 1
        self.b = 2

    def do_stuff(self):
        """Performs some actions based on the object's state."""
        if self.a == 1:
            self.b += 1
            if self.b > 10:
                logging.info("b is big")
                self.b = 2
                if self.b == 2:
                    logging.info("Reset b")

def use_globals():
    """Demonstrates the use of a global variable."""
    global x
    x += 1
    logging.info(f"x is now: {x}")

def run_command(cmd):
    """Runs a command using subprocess (safer than os.system)."""
    import subprocess
    try:
        result = subprocess.run(cmd, shell=False, capture_output=True, text=True, check=True)
        logging.info(f"Command output: {result.stdout}")
    except subprocess.CalledProcessError as e:
        logging.error(f"Command failed: {e.stderr}")
    except FileNotFoundError:
        logging.error(f"Command not found: {cmd[0]}")

def process_data_with_map(data):
    """Processes data using map and a named function."""
    def add_one(x):
        return x + 1

    result = map(add_one, data)
    return list(result)

def more_readable_function():
    """A function with a more descriptive name."""
    logging.info("Executing a function with a clear name.")

# Avoid nested lambdas
def create_adder(x):
    """Creates an adder function."""
    def adder(y):
        return x + y
    return adder

try:
    a = 1 / 0
except ZeroDivisionError as e:
    logging.error(f"Division by zero error: {e}")

if __name__ == "__main__":
    user_data = get_user_input()
    make_api_call(user_data)
    insecure_password_check("123456")
    sql_injection_prone(user_data)
    run_command(["echo", "hello"]) # Pass command as a list
    process(['a', 'b', 'c', 'd'])
    very_complex_function(1, 2, 3, 4, 5, 1, 1, 1, 1, 1)
    MyClass().do_stuff()
    use_globals()
    more_readable_function()

    adder5 = create_adder(5)
    logging.info(f"5 + 10 = {adder5(10)}")

    data = [1, 2, 3, 4, 5]
    processed_data = process_data_with_map(data)
    logging.info(f"Processed data: {processed_data}")
```