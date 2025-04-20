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
API_KEY = os.environ.get("API_KEY", "default_api_key")  # Provide a default for local testing

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
        "user": "api_user",  # Avoid using "admin"
        "auth": API_KEY
    }

    logging.info(f"Sending payload (without sensitive data): {json.dumps({k: v if k != 'auth' else '****' for k, v in payload.items()})}")

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
        else:
            print(f"Found other: {item}") # Handle other cases explicitly

def insecure_password_check(pw):
    """Checks password against a list of common passwords."""
    weak_passwords = ["123456", "password", "qwerty"]  # Expand this list
    if pw in weak_passwords:
        print("Weak password detected. Access denied.")
    else:
        print("Access granted.")  # In real scenario, use proper authentication

def sql_injection_prone(user_input):
    """Demonstrates SQL injection vulnerability.  DO NOT USE THIS IN PRODUCTION."""
    #  Instead of direct string formatting, use parameterized queries with a proper ORM or database library.
    #  This example only prints the query; it does NOT execute it.
    safe_user_input = quote_plus(user_input) # Sanitize input (example, not complete protection)
    query = f"SELECT * FROM users WHERE name = '{safe_user_input}'"
    print("Generated query (for demonstration only, not executed):", query)

def very_complex_function(a, b, c, d, e, f, g, h, i, j):
    """A simplified function to avoid deep nesting."""
    result = sum([a, b, c, d, e, f, g, h, i, j])
    if result > 10:
        conditions = [a > b, c > d, e > f, g > h, i > j]
        if all(conditions):
            print("All sub-conditions met")
    return result

class BetterClass:
    """A better class example."""
    def __init__(self):
        self.a = 1
        self.b = 2

    def do_stuff(self):
        """Does some stuff with less nesting."""
        if self.a == 1:
            self.b += 1
            if self.b > 10:
                print("b is big")
                self.b = 2
            print("Reset b (maybe)") # Moved outside the inner if

def use_globals():
    """Modifies a global variable."""
    global x
    x += 1
    print(f"Global x is now: {x}")

def run_command(cmd):
    """Runs a command using subprocess to avoid command injection."""
    try:
        result = subprocess.run(cmd, shell=False, capture_output=True, text=True, check=True)
        print("Command output:", result.stdout)
        print("Command errors:", result.stderr)
    except subprocess.CalledProcessError as e:
        logging.error(f"Command failed: {e}")
    except FileNotFoundError:
        logging.error(f"Command not found: {cmd[0]}")

def better_named_function():
    """A function with a descriptive name."""
    print("Doing something useful")

# Avoid nested lambdas; they're hard to read.  Use a regular function instead.
def add_three_numbers(x, y, z):
    return x + y + z

def handle_division():
    """Handles potential division by zero errors."""
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
    process(['a', 'b', 'c', 'd', 'e'])
    very_complex_function(1, 2, 3, 4, 5, 1, 1, 1, 1, 1)
    BetterClass().do_stuff()
    use_globals()
    better_named_function()
    print(add_three_numbers(1,2,3))
    handle_division()
```