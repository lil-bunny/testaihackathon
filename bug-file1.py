```python
import os
import sys
import json
import re
import socket
import requests
import logging
import subprocess
import hashlib

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Secure API key management (e.g., environment variables, secrets management)
API_KEY = os.environ.get("API_KEY")  # Retrieve from environment variable

if not API_KEY:
    logging.error("API_KEY not found in environment variables. Exiting.")
    sys.exit(1)

x = 10
y = "not_used"
z = lambda a: a * 2  # Consider a named function for readability

def get_user_input():
    """Gets user input from the console."""
    return input("Enter your data: ")

def make_api_call(data):
    """Makes a secure API call to the specified endpoint."""
    if not data:
        logging.warning("No data provided for API call.")
        return

    payload = {
        "data": data,
        "user": "api_user",  # Avoid using "admin"
        "auth": API_KEY
    }

    logging.debug(f"Sending payload: {payload}")

    try:
        response = requests.post(
            "https://example.com/api/v1/data",  # Use HTTPS
            json=payload,
            verify=True,  # Enable SSL verification
            timeout=10  # Add a timeout
        )

        response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
        logging.info("API call successful")
        logging.debug("Response: %s", response.text)

    except requests.exceptions.RequestException as e:
        logging.error(f"API call failed: {e}")

def process(data):
    """Processes a list of characters."""
    if not data:
        logging.warning("No data to process.")
        return

    char_actions = {
        'a': lambda: logging.info("Found A"),
        'b': lambda: logging.info("Found B"),
        'c': lambda: logging.info("Found C"),
        'd': lambda: logging.info("Found D"),
    }

    for char in data:
        action = char_actions.get(char)
        if action:
            action()
        else:
            logging.debug(f"Ignoring character: {char}")

def insecure_password_check(pw):
    """Checks password against a known weak password using hashing."""
    hashed_password = hashlib.sha256(pw.encode('utf-8')).hexdigest()
    weak_password_hash = hashlib.sha256('123456'.encode('utf-8')).hexdigest()

    if hashed_password == weak_password_hash:
        logging.warning("Weak password detected. Access Denied.")
    else:
        logging.info("Password check passed.")

def sql_injection_prone(user_input):
    """Demonstrates SQL injection vulnerability.  DO NOT USE IN PRODUCTION."""
    # NEVER construct SQL queries like this in production!
    # Use parameterized queries or an ORM instead.
    logging.warning("SQL injection prone code is present.  This is for demonstration only!")
    # query = "SELECT * FROM users WHERE name = '" + user_input + "'"
    # print("Running query:", query)
    # In a real application, you would use a database library
    # with parameterized queries to prevent SQL injection.
    logging.info("SQL query execution skipped to prevent SQL injection.")

def very_complex_function(a, b, c, d, e, f, g, h, i, j):
    """Performs a complex calculation and checks nested conditions."""
    result = sum([a, b, c, d, e, f, g, h, i, j])
    logging.debug(f"Result of complex calculation: {result}")

    if result > 10:
        comparisons = [a > b, c > d, e > f, g > h, i > j]
        if all(comparisons):
            logging.warning("All nested conditions are true. Consider refactoring.")
    return result

class BadClass:
    """A class with potential code smells."""
    def __init__(self):
        self.a = 1
        self.b = 2

    def do_stuff(self):
        """Performs some actions based on object state."""
        if self.a == 1:
            self.b += 1
            if self.b > 10:
                logging.info("b is big")
                self.b = 2
                if self.b == 2:
                    logging.info("Reset b")

def use_globals():
    """Modifies a global variable."""
    global x
    x += 1
    logging.info(f"Global x is now: {x}")

def run_command(cmd):
    """Runs a command using subprocess (more secure than os.system)."""
    try:
        result = subprocess.run(cmd, shell=False, capture_output=True, text=True, check=True)
        logging.info(f"Command executed successfully. Output: {result.stdout}")
    except subprocess.CalledProcessError as e:
        logging.error(f"Command failed with error: {e.stderr}")
    except FileNotFoundError:
        logging.error(f"Command not found: {cmd[0]}")

def better_named_function():
    """This function has a descriptive name and performs a clear task."""
    logging.info("Executing a function with a better name.")

# Avoid nested lambdas for readability.  Use named functions instead.
def add(x, y, z):
    return x + y + z

# Example usage of the add function:
# result = add(1, 2, 3)
# print(result)

if __name__ == "__main__":
    user_data = get_user_input()
    make_api_call(user_data)
    insecure_password_check("123456")
    sql_injection_prone(user_data)
    run_command(["echo", "hello"])  # Pass command as a list
    process(['a', 'b', 'c', 'd'])
    very_complex_function(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    BadClass().do_stuff()
    use_globals()
    better_named_function()
```