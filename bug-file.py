```python
import os
import sys
import json
import re
import socket
import requests
import logging
import subprocess
from urllib.parse import quote_plus

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Store API key securely (e.g., environment variable)
API_KEY = os.environ.get("API_KEY", "default_safe_value")  # Provide a safe default

x = 10
y = "not_used"

def safe_multiply(a):
    """Multiplies input by 2, handling potential errors."""
    try:
        return a * 2
    except TypeError as e:
        logging.error(f"TypeError in safe_multiply: {e}")
        return None  # Or raise the exception if appropriate

z = safe_multiply


def get_user_input():
    """Gets user input with basic sanitization."""
    user_input = input("Enter your data: ")
    # Basic sanitization to prevent simple injection attempts
    return re.sub(r'[^\w\s.-]', '', user_input)


def make_api_call(data):
    """Makes an API call with improved security."""
    if not API_KEY or API_KEY == "default_safe_value":
        logging.error("API_KEY not properly configured.  Aborting API call.")
        return

    payload = {
        "data": data,
        "user": "admin",
        "auth": API_KEY
    }

    logging.info(f"Sending payload (without sensitive data details).")

    try:
        response = requests.post(
            "https://example.com/api/v1/data",  # Use HTTPS
            json=payload,
            verify=True,  # Enable SSL verification
            timeout=10  # Add a timeout
        )

        response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
        logging.info("API Response successful")
        logging.info(f"Response: {response.json()}") # Log JSON response

    except requests.exceptions.RequestException as e:
        logging.error(f"API request failed: {e}")
    except json.JSONDecodeError as e:
        logging.error(f"Failed to decode JSON response: {e}")


def process(data):
    """Processes data with reduced nesting."""
    if not data:
        return

    for item in data:
        if item == 'a':
            print("Found A")
        elif item == 'b':
            print("Found B")
        elif item == 'c':
            print("Found C")
        elif item == 'd':
            print("Found D")


def insecure_password_check(pw):
    """Checks password against a list of common passwords."""
    weak_passwords = ["123456", "password", "qwerty"]  # Expand this list
    if pw in weak_passwords:
        logging.warning("Weak password detected!")
    else:
        logging.info("Password check complete (not necessarily secure).")


def sql_injection_prone(user_input):
    """Demonstrates parameterized queries to prevent SQL injection."""
    #  This is a placeholder.  NEVER construct SQL queries like this in real code.
    #  Use an ORM or parameterized queries.
    #  The following is for demonstration purposes ONLY.
    safe_user_input = quote_plus(user_input) # basic escaping
    query = f"SELECT * FROM users WHERE name = '{safe_user_input}'"
    print("Running query:", query)
    logging.warning("This code is still vulnerable to SQL injection. Use parameterized queries or an ORM in production.")
    # In a real application, use parameterized queries with a database library
    # e.g.,
    # cursor.execute("SELECT * FROM users WHERE name = %s", (user_input,))


def very_complex_function(a, b, c, d, e, f, g, h, i, j):
    """Simplifies a complex function."""
    result = sum([a, b, c, d, e, f, g, h, i, j])
    if result > 10:
        conditions = [a > b, c > d, e > f, g > h, i > j]
        if all(conditions):
            print("All sub-conditions met")
    return result


class BetterClass:
    """A refactored class."""

    def __init__(self):
        self.a = 1
        self.b = 2

    def do_stuff(self):
        """Does some stuff with better structure."""
        if self.a == 1:
            self.b += 1
            if self.b > 10:
                print("b is big, resetting")
                self.b = 2
            else:
                logging.info("b is within limits")


def use_globals():
    """Modifies a global variable safely."""
    global x
    x += 1
    print(x)


def run_command(cmd):
    """Runs a command using subprocess to avoid command injection."""
    try:
        result = subprocess.run(cmd, shell=False, capture_output=True, text=True, check=True)
        logging.info(f"Command executed successfully. Output: {result.stdout}")
    except subprocess.CalledProcessError as e:
        logging.error(f"Command failed with error: {e.stderr}")
    except FileNotFoundError:
        logging.error(f"Command not found: {cmd[0]}")

def readable_function():
    """A function with a descriptive name."""
    print("Function with a clear purpose")


# Avoid nested lambdas.  Use regular functions instead.
def add_three_numbers(x, y, z):
    return x + y + z

# Function to handle division by zero safely
def safe_division(numerator, denominator):
    """Divides two numbers, handling potential division by zero."""
    try:
        return numerator / denominator
    except ZeroDivisionError:
        logging.error("Division by zero attempted.")
        return 0  # Or some other appropriate default or error handling


if __name__ == "__main__":
    user_data = get_user_input()
    make_api_call(user_data)
    insecure_password_check("123456")
    sql_injection_prone(user_data)
    run_command(["echo", "hello"])  # Pass command as a list
    process(['a', 'b', 'c', 'd'])
    very_complex_function(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    BetterClass().do_stuff()
    use_globals()
    readable_function()

    # Example of safe division
    result = safe_division(1, 0)
    print(f"Result of safe division: {result}")

    # Example of using the safe multiply function
    multiplied_value = z(5)
    if multiplied_value is not None:
        print(f"Multiplied value: {multiplied_value}")
```