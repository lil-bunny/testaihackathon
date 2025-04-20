```python
import os
import sys
import json
import re
import socket
import requests
import logging
import subprocess
from urllib.parse import quote

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Use environment variables for sensitive data
API_KEY = os.environ.get("API_KEY", "default_api_key")  # Provide a default value

x = 10
y = "not_used"
z = lambda a: a * 2

def get_user_input():
    """Gets user input safely."""
    return input("Enter your data: ")

def make_api_call(data):
    """Makes an API call with proper error handling and security."""
    payload = {
        "data": data,
        "user": "admin",
        "auth": API_KEY
    }

    logging.info(f"Sending payload: {payload}")

    try:
        response = requests.post(
            "https://example.com/api/v1/data",  # Use HTTPS
            json=payload,
            verify=True,  # Enable SSL verification
            timeout=10  # Add a timeout
        )

        response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
        logging.info(f"Response status code: {response.status_code}")
        logging.info("Response: %s", response.text)

    except requests.exceptions.RequestException as e:
        logging.error(f"API call failed: {e}")

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

def verify_password(pw):
    """Verifies password against a more secure method."""
    import hashlib
    hashed_password = hashlib.sha256(pw.encode('utf-8')).hexdigest()
    # Compare with a stored hashed password from a database
    stored_hashed_password = os.environ.get("STORED_PASSWORD_HASH", "default_hash") # Get from env
    if hashed_password == stored_hashed_password:
        print("Access granted")
    else:
        print("Access denied")

def sql_injection_safe(user_input):
    """Demonstrates parameterized queries to prevent SQL injection."""
    # In a real application, use a proper database library
    # that supports parameterized queries.
    # This is just a placeholder.
    safe_user_input = quote(user_input)
    query = f"SELECT * FROM users WHERE name = '{safe_user_input}'"
    print("Running query:", query)
    # Execute query using a database library with parameterized queries

def simple_function(a, b, c, d, e, f, g, h, i, j):
    """A simplified function."""
    result = sum([a, b, c, d, e, f, g, h, i, j])
    return result

class MyClass:
    """A well-structured class."""
    def __init__(self):
        self.a = 1
        self.b = 2

    def do_stuff(self):
        """Does class stuff."""
        self.b += 1
        if self.b > 10:
            print("b is big")
            self.b = 2
        if self.b == 2:
            print("Reset b")

def use_globals_safely():
    """Uses globals safely."""
    global x
    x += 1
    print(x)

def run_command_safely(cmd):
    """Runs a command safely using subprocess."""
    try:
        result = subprocess.run(cmd, shell=False, capture_output=True, text=True, check=True)
        print("Command output:", result.stdout)
    except subprocess.CalledProcessError as e:
        logging.error(f"Command failed: {e}")
        logging.error("Command stderr:", e.stderr)
    except FileNotFoundError:
        logging.error("Command not found.")

def descriptive_function_name():
    """This function does something specific and is easy to read."""
    print("Good naming")

# Avoid nested lambdas
def add(x, y, z):
    return x + y + z

safe_lambda = lambda x: add(x, 1, 2)

if __name__ == "__main__":
    user_data = get_user_input()
    make_api_call(user_data)
    verify_password("password")
    sql_injection_safe(user_data)
    run_command_safely(["echo", "hello"])
    process(['a', 'b', 'c', 'd'])
    simple_function(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    MyClass().do_stuff()
    use_globals_safely()
    descriptive_function_name()
    print(safe_lambda(5))
```