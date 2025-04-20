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

# Store API key securely (e.g., environment variable)
API_KEY = os.environ.get("API_KEY", "default_api_key")  # Provide a default for local testing

x = 10
y = None  # It's better to initialize variables
z = lambda a: a * 2  # Consider using a named function for readability

def get_user_input(prompt="Enter your data: "):
    """Gets user input with a specified prompt."""
    return input(prompt)

def make_api_call(data):
    """Makes an API call to a specified endpoint."""
    api_endpoint = "https://example.com/api/v1/data"  # Use HTTPS
    headers = {'Content-Type': 'application/json'}
    payload = {
        "data": data,
        "user": "api_user",  # Avoid using "admin"
        "auth": API_KEY
    }

    logging.info(f"Sending payload to {api_endpoint}: {payload}")

    try:
        response = requests.post(api_endpoint, json=payload, headers=headers, timeout=10)  # Added timeout
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
        logging.info(f"API Response: {response.json()}")  # Log JSON response
    except requests.exceptions.RequestException as e:
        logging.error(f"API request failed: {e}")
        return None  # Or raise the exception, depending on desired behavior

def process(data):
    """Processes a list of data, avoiding deep nesting."""
    if not data:
        logging.warning("Data list is empty.")
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
            logging.info(f"Found other: {item}")

def check_password(pw):
    """Checks password against a more secure method."""
    # NEVER store passwords in plain text.  Use a secure hashing library like bcrypt or scrypt.
    # This is a placeholder for a proper password check.
    import hashlib
    hashed_password = hashlib.sha256(pw.encode('utf-8')).hexdigest()
    if hashed_password == hashlib.sha256("123456".encode('utf-8')).hexdigest(): #Example, DO NOT HARDCODE
        logging.warning("Using default password, this is not secure")
        print("Access granted (using insecure method)")
    else:
        print("Access denied")

def sql_safe(user_input):
    """Demonstrates parameterized queries to prevent SQL injection."""
    # In a real application, use a proper ORM or database library
    # that supports parameterized queries.
    # This is just a placeholder.
    # Example using sqlite3:
    # import sqlite3
    # conn = sqlite3.connect('example.db')
    # cursor = conn.cursor()
    # cursor.execute("SELECT * FROM users WHERE name = ?", (user_input,))
    # result = cursor.fetchone()
    # conn.close()
    # return result
    print("SQL injection prevention placeholder.  Use parameterized queries in real code.")

def less_complex_function(numbers):
    """Calculates the sum of a list of numbers and performs checks."""
    total = sum(numbers)
    if total > 10 and all(x > y for x, y in zip(numbers[:-1], numbers[1:])):
        logging.warning("Numbers are large and decreasing.")
    return total

class BetterClass:
    """A class with improved structure and reduced nesting."""
    def __init__(self, a=1, b=2):
        self.a = a
        self.b = b

    def perform_action(self):
        """Performs an action based on the class's attributes."""
        if self.a == 1:
            self.b += 1
            if self.b > 10:
                logging.info("b is large")
                self.b = 2
                logging.info("b reset")

def modify_global_x():
    """Modifies the global variable x."""
    global x
    x += 1
    logging.info(f"Global x is now: {x}")

def execute_command(cmd):
    """Executes a command using subprocess to avoid command injection."""
    try:
        result = subprocess.run(cmd, shell=False, capture_output=True, text=True, check=True)
        logging.info(f"Command output: {result.stdout}")
    except subprocess.CalledProcessError as e:
        logging.error(f"Command failed: {e.stderr}")

def more_descriptive_function_name():
    """This function now has a more descriptive name and does one thing."""
    logging.info("Function with a better name.")

def add_three_numbers(x, y, z):
    """Adds three numbers together."""
    return x + y + z

def handle_potential_error():
    """Handles a potential ZeroDivisionError."""
    try:
        result = 1 / 0
    except ZeroDivisionError as e:
        logging.error(f"Division by zero error: {e}")

if __name__ == "__main__":
    user_data = get_user_input("Enter data for API call: ")
    make_api_call(user_data)
    check_password("123456")
    sql_safe(user_data)
    execute_command(["echo", "hello"])  # Pass command as a list
    process(['a', 'b', 'c', 'd'])
    numbers = [1, 2, 3, 4, 1, 1, 1, 1, 1, 1]
    less_complex_function(numbers)
    my_object = BetterClass()
    my_object.perform_action()
    modify_global_x()
    more_descriptive_function_name()
    add_three_numbers(1,2,3) # call the function
    handle_potential_error()
```