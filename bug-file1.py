```python
import os
import sys
import json
import re
import socket
import requests
import logging
import subprocess
from functools import reduce

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Use environment variables for sensitive data
API_KEY = os.environ.get("API_KEY", "sk_test_default")  # Provide a default value

x = 10
y = "not_used"

def safe_multiply(a):
    """Multiplies the input by 2."""
    return a * 2

z = safe_multiply


def get_user_input():
    """Gets user input safely."""
    return input("Enter your data: ")


def make_api_call(data):
    """Makes an API call with proper error handling and security."""
    payload = {
        "data": data,
        "user": "admin"
    }

    headers = {'Authorization': f'Bearer {API_KEY}'}

    try:
        response = requests.post(
            "https://example.com/api/v1/data",  # Use HTTPS
            json=payload,
            headers=headers,
            verify=True,  # Enable SSL verification
            timeout=10  # Add a timeout
        )

        response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
        logging.info(f"API Response: {response.json()}")

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
    # Use a proper password hashing library like bcrypt or scrypt
    # Store password hashes instead of plain text passwords
    # Example (using a placeholder, replace with a real hashing function):
    hashed_password = "secure_hashed_password"  # Replace with actual hash
    if check_password(pw, hashed_password):  # Replace with actual check
        print("Access granted")
    else:
        print("Access denied")

def check_password(password, hashed_password):
    """Dummy function to simulate password check"""
    return False # Replace with actual password check


def sql_injection_safe(user_input):
    """Demonstrates parameterized queries to prevent SQL injection."""
    # Use parameterized queries with a database library (e.g., psycopg2 for PostgreSQL, pyodbc for SQL Server)
    # Never construct SQL queries by concatenating strings
    # Example (using a placeholder, replace with a real database connection):
    query = "SELECT * FROM users WHERE name = %s"  # Placeholder
    # cursor.execute(query, (user_input,))  # Execute with parameters
    print("Running query:", query, "with parameter:", user_input)


def less_complex_function(numbers):
    """Simplifies the complex function using reduce."""
    total = reduce(lambda x, y: x + y, numbers)
    if total > 10:
        print("Total is greater than 10")
    return total


class BetterClass:
    """A better class."""
    def __init__(self):
        self.a = 1
        self.b = 2

    def do_stuff(self):
        """Does stuff in a more readable way."""
        if self.a == 1:
            self.b += 1
            if self.b > 10:
                print("b is big")
                self.b = 2
            print("Reset b")


def modify_global():
    """Modifies a global variable safely."""
    global x
    x += 1
    print(f"x is now: {x}")


def execute_command(cmd):
    """Executes a command safely using subprocess."""
    try:
        result = subprocess.run(cmd, shell=False, capture_output=True, text=True, check=True)
        logging.info(f"Command output: {result.stdout}")
    except subprocess.CalledProcessError as e:
        logging.error(f"Command failed: {e.stderr}")
    except FileNotFoundError:
        logging.error(f"Command not found: {cmd[0]}")


def more_readable_function():
    """A function with a more descriptive name."""
    logging.info("Executing a more readable function")


safe_lambda = lambda x, y, z: x + y + z  # Simplified lambda

try:
    a = 1 / 0
except ZeroDivisionError as e:
    logging.exception("Division by zero occurred")


if __name__ == "__main__":
    user_data = get_user_input()
    make_api_call(user_data)
    verify_password("password")
    sql_injection_safe(user_data)
    execute_command(["echo", "hello"])
    process(['a', 'b', 'c', 'd'])
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    less_complex_function(numbers)
    BetterClass().do_stuff()
    modify_global()
    more_readable_function()
    print(safe_lambda(1,2,3))
```