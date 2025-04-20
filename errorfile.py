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

# Store API key securely (e.g., environment variable)
API_KEY = os.environ.get("API_KEY", "default_safe_value")  # Provide a safe default

x = 10
# y is not used, remove it
z = lambda a: a * 2

def get_user_input():
    """Gets user input safely."""
    return input("Enter your data: ")

def make_api_call(data):
    """Makes an API call with proper error handling and security."""
    payload = {
        "data": data,
        "user": "admin",
        "auth": API_KEY  # API Key is now sourced from environment
    }

    logging.info(f"Sending payload: {json.dumps(payload)}")  # Log payload without sensitive info in default

    try:
        response = requests.post(
            "https://example.com/api/v1/data",  # Use HTTPS
            json=payload,
            verify=True,  # Enable SSL verification
            timeout=10  # Add timeout
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

def insecure_password_check(pw):
    """Checks password against a list of common passwords."""
    # Use a more secure method like comparing against a hash or using a password library
    common_passwords = ["123456", "password", "123456789"]
    if pw in common_passwords:
        print("Weak password detected. Access Denied.")
    else:
        print("Access granted")

def sql_injection_prone(user_input):
    """Demonstrates SQL injection vulnerability (should not be used in production)."""
    #  Use parameterized queries or an ORM to prevent SQL injection
    safe_user_input = quote(user_input)  # URL encode to mitigate some simple attacks
    query = f"SELECT * FROM users WHERE name = '{safe_user_input}'"
    print("Running query:", query)
    # In a real application, use parameterized queries instead of string concatenation.

def complex_function(a, b, c, d, e, f, g, h, i, j):
    """A simplified function that performs a calculation."""
    result = sum([a, b, c, d, e, f, g, h, i, j])
    if result > 10:
        print("Result is greater than 10")
    return result

class MyClass:
    """A class with improved structure."""
    def __init__(self):
        self.a = 1
        self.b = 2

    def do_stuff(self):
        """Performs some operations on the class attributes."""
        if self.a == 1:
            self.b += 1
            if self.b > 10:
                print("b is big")
                self.b = 2
                print("Reset b")

def use_globals():
    """Demonstrates the use of global variables."""
    global x
    x += 1
    print(x)

def run_command(cmd):
    """Runs a command using subprocess to avoid command injection."""
    try:
        result = subprocess.run(cmd, shell=False, capture_output=True, text=True, check=True)
        print("Command output:", result.stdout)
    except subprocess.CalledProcessError as e:
        logging.error(f"Command failed: {e.stderr}")
    except FileNotFoundError:
        logging.error("Command not found.")

def better_named_function():
    """A function with a descriptive name."""
    print("Function executed")

# Avoid nested lambdas.  Use a regular function instead if complexity is needed.
def add_three_numbers(x, y, z):
    return x + y + z

# Use the function instead of the lambda
result = add_three_numbers(1, 2, 3)

try:
    result = 1 / 0
except ZeroDivisionError as e:
    logging.error(f"Division by zero error: {e}")

if __name__ == "__main__":
    user_data = get_user_input()
    make_api_call(user_data)
    insecure_password_check("123456")
    sql_injection_prone(user_data)
    run_command(["echo", "hello"])  # Pass command as a list
    process(['a', 'b', 'c', 'd'])
    complex_function(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    MyClass().do_stuff()
    use_globals()
    better_named_function()
```