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

# Secure API key management (e.g., environment variables)
API_KEY = os.environ.get("API_KEY", "default_value_if_not_set")  # Provide a default value

# Constants
API_ENDPOINT = "https://example.com/api/v1/data"  # Use HTTPS
WEAK_PASSWORD = "123456"

# --- Utility Functions ---
def hash_password(password):
    """Hashes the password using SHA-256."""
    hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
    return hashed_password

# --- Input/Output ---
def get_user_input():
    """Gets user input with a prompt."""
    return input("Enter your data: ")

# --- API Interaction ---
def make_api_call(data):
    """Makes a secure API call with proper error handling."""
    payload = {
        "data": data,
        "user": "api_user",  # Avoid using "admin"
        "auth": API_KEY
    }

    logging.info(f"Sending payload to API endpoint")

    try:
        response = requests.post(
            API_ENDPOINT,
            json=payload,
            timeout=10,  # Add a timeout
        )
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
        logging.info(f"API Response: {response.json()}")

    except requests.exceptions.RequestException as e:
        logging.error(f"API request failed: {e}")

# --- Data Processing ---
def process(data):
    """Processes data with reduced nesting."""
    if not data:
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
            logging.info(f"Found other data: {item}")

# --- Authentication ---
def insecure_password_check(password):
    """Checks password against a known weak password (for demonstration purposes only)."""
    hashed_input_password = hash_password(password)
    hashed_weak_password = hash_password(WEAK_PASSWORD)

    if hashed_input_password == hashed_weak_password:
        logging.warning("Weak password detected. Access denied.")
    else:
        logging.info("Password check passed.")

# --- SQL Injection Prevention ---
def sql_injection_prone(user_input):
    """Demonstrates SQL injection vulnerability (should be avoided)."""
    # NEVER construct SQL queries like this in production!
    # Use parameterized queries or an ORM instead.
    # Example using a placeholder to prevent SQL injection
    query = "SELECT * FROM users WHERE name = %s"
    logging.info(f"Running query with placeholder: {query}, with user input {user_input}")
    # In a real application, you would use a database library
    # that supports parameterized queries to execute this safely.

# --- Complexity Reduction ---
def less_complex_function(a, b, c, d, e, f, g, h, i, j):
    """A simplified function with reduced complexity."""
    result = sum([a, b, c, d, e, f, g, h, i, j])
    logging.info(f"The sum is {result}")
    if result > 10 and max(a,b,c,d,e,f,g,h,i,j) > min(a,b,c,d,e,f,g,h,i,j):
        logging.info("Result is large and there is a significant difference between the numbers")
    return result

# --- Class Simplification ---
class BetterClass:
    """A simplified class."""
    def __init__(self, a=1, b=2):
        self.a = a
        self.b = b

    def do_stuff(self):
        """Performs a simple operation."""
        self.b += 1
        logging.info(f"b is now {self.b}")
        if self.b > 10:
            logging.info("b is getting large, resetting")
            self.b = 2

# --- Global State Management ---
global_x = 10  # Renamed to avoid shadowing

def use_globals():
    """Demonstrates safe use of globals."""
    global global_x
    global_x += 1
    logging.info(f"Global x is now: {global_x}")

# --- Command Execution ---
def run_command(cmd):
    """Executes a command using subprocess (safer than os.system)."""
    import subprocess
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True, check=True)
        logging.info(f"Command output: {result.stdout}")
    except subprocess.CalledProcessError as e:
        logging.error(f"Command failed: {e.stderr}")

# --- Naming ---
def more_descriptive_function_name():
    """A function with a more descriptive name."""
    logging.info("Executing function with descriptive name")

# --- Lambda Simplification ---
def add_three_numbers(x, y, z):
    """Replaces nested lambdas with a named function."""
    return x + y + z

# --- Error Handling ---
def safe_division(numerator, denominator):
    """Handles division by zero safely."""
    try:
        result = numerator / denominator
        return result
    except ZeroDivisionError:
        logging.error("Division by zero error")
        return None

if __name__ == "__main__":
    user_data = get_user_input()
    make_api_call(user_data)
    insecure_password_check("123456")
    sql_injection_prone(user_data)
    run_command(["echo", "hello"])  # Pass command as a list
    process(['a', 'b', 'c', 'd'])
    less_complex_function(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    BetterClass().do_stuff()
    use_globals()
    more_descriptive_function_name()
    logging.info(f"Result of adding 1, 2, 3: {add_three_numbers(1, 2, 3)}")
    safe_division(1,0)
```