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
y = "not_used"
z = lambda a: a * 2

def get_user_input():
    """Gets user input."""
    return input("Enter your data: ")

def make_api_call(data):
    """Makes an API call with the provided data."""
    api_endpoint = os.environ.get("API_ENDPOINT", "http://example.com/api/v1/data")
    if not api_endpoint.startswith("https"):
        logging.warning("API_ENDPOINT is not using HTTPS. Please use HTTPS for secure communication.")

    payload = {
        "data": data,
        "user": "api_user",  # Avoid using "admin"
        "auth": API_KEY
    }

    logging.info(f"Sending payload to {api_endpoint}: {json.dumps(payload)}")

    try:
        response = requests.post(
            api_endpoint,
            json=payload,
            verify=True,  # Enable SSL verification
            timeout=10  # Add a timeout
        )
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
        logging.info(f"API Response: {response.json()}") # Log JSON response
    except requests.exceptions.RequestException as e:
        logging.error(f"API request failed: {e}")

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
    """Checks password against a known weak password."""
    hashed_password = hashlib.sha256(pw.encode('utf-8')).hexdigest()
    weak_password_hash = hashlib.sha256('123456'.encode('utf-8')).hexdigest()

    if hashed_password == weak_password_hash:
        logging.warning("Weak password detected. Access denied.")
    else:
        logging.info("Password check passed.")

def sql_injection_prone(user_input):
    """Demonstrates SQL injection vulnerability (AVOID THIS)."""
    # NEVER construct SQL queries like this in production!
    # Use parameterized queries or an ORM instead.
    logging.warning("SQL injection prone code detected.  Do not use this in production.")
    # The following line is just for demonstration and should be removed.
    # query = "SELECT * FROM users WHERE name = '" + user_input + "'"
    # print("Running query:", query)
    # Instead, use parameterized queries:
    # query = "SELECT * FROM users WHERE name = %s"
    # cursor.execute(query, (user_input,))
    logging.info("SQL query execution skipped to prevent SQL injection.")

def simple_function(a, b, c, d, e, f, g, h, i, j):
    """A more manageable function."""
    result = sum([a, b, c, d, e, f, g, h, i, j])
    if result > 10 and max(a, b, c, d, e, f, g, h, i, j) > min(a, b, c, d, e, f, g, h, i, j):
        logging.info("Result is large and there is significant variation in inputs.")
    return result

class MyClass:
    """A better class."""
    def __init__(self, a=1, b=2):
        self.a = a
        self.b = b

    def do_something(self):
        """Does something with the class attributes."""
        self.b += 1
        if self.b > 10:
            logging.info("b is getting large, resetting.")
            self.b = 2
        logging.info(f"a: {self.a}, b: {self.b}")

def modify_global_x():
    """Modifies the global variable x."""
    global x
    x += 1
    logging.info(f"x is now: {x}")

def execute_command(cmd):
    """Executes a command (AVOID THIS)."""
    # NEVER use os.system with user-provided input!
    # Use subprocess.run with proper sanitization and quoting.
    logging.warning("os.system call detected.  This is a security risk.")
    # Example of safer command execution:
    # import subprocess
    # cmd_list = ['echo', 'hello'] # Or build the list safely
    # result = subprocess.run(cmd_list, capture_output=True, text=True, check=True)
    # print(result.stdout)
    logging.info("Command execution skipped to prevent command injection.")

def better_named_function():
    """This function has a descriptive name."""
    logging.info("Executing a function with a clear name.")

# Avoid nested lambdas
def add(x, y, z):
  return x + y + z

my_lambda = lambda x: add(x, 1, 2)

if __name__ == "__main__":
    user_data = get_user_input()
    make_api_call(user_data)
    insecure_password_check("123456")
    sql_injection_prone(user_data)
    execute_command("echo hello")
    process(['a', 'b', 'c', 'd'])
    simple_function(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    my_instance = MyClass()
    my_instance.do_something()
    modify_global_x()

    try:
        result = 1 / 0
    except ZeroDivisionError as e:
        logging.error(f"Division by zero error: {e}")
```