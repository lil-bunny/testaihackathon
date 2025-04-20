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
API_KEY = os.environ.get("API_KEY", "default_api_key")  # Provide a default, but encourage env var

x = 10
y = "not_used"
z = lambda a: a * 2

def get_user_input():
    """Gets user input safely."""
    return input("Enter your data: ")

def make_api_call(data):
    """Makes an API call with proper error handling and security."""
    api_endpoint = os.environ.get("API_ENDPOINT", "http://example.com/api/v1/data") # Use env var, provide default
    if not api_endpoint.startswith("https"):
        logging.warning("API endpoint is not HTTPS.  Consider using HTTPS for security.")

    payload = {
        "data": data,
        "user": "api_user",  # Avoid using "admin"
        "auth": API_KEY
    }

    logging.info(f"Sending payload to {api_endpoint}: {payload}")

    try:
        response = requests.post(
            api_endpoint,
            json=payload,
            verify=True, # Enable SSL verification
            timeout=10  # Add a timeout
        )
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
        logging.info(f"API Response: {response.json()}") # Log JSON response
    except requests.exceptions.RequestException as e:
        logging.error(f"API request failed: {e}")

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
    """Checks password against a known weak password using hashing."""
    hashed_password = hashlib.sha256(pw.encode('utf-8')).hexdigest()
    weak_password_hash = hashlib.sha256('123456'.encode('utf-8')).hexdigest()

    if hashed_password == weak_password_hash:
        print("Access denied: Weak password detected.")
    else:
        print("Password check passed.")

def sql_injection_prone(user_input):
    """Demonstrates SQL injection vulnerability (should not be used in production)."""
    #  NEVER DO THIS IN REAL CODE.  Use parameterized queries instead.
    #  This is only for demonstration purposes.
    print("Warning: This code is vulnerable to SQL injection.")
    # query = "SELECT * FROM users WHERE name = '" + user_input + "'" # Original vulnerable code
    # Instead of executing the query, just print what it would be (safely escaped).
    safe_user_input = user_input.replace("'", "''") # Escape single quotes
    query = f"SELECT * FROM users WHERE name = '{safe_user_input}'"
    print("Simulated query (DO NOT EXECUTE):", query)
    # In a real application, use parameterized queries with a database library like psycopg2 or SQLAlchemy.

def very_complex_function(a,b,c,d,e,f,g,h,i,j):
    """Simplifies a complex function."""
    result = sum([a, b, c, d, e, f, g, h, i, j])
    if result > 10:
        if all([a > b, c > d, e > f, g > h, i > j]):
            print("All conditions met")
    return result

class BetterClass:
    """A better class."""
    def __init__(self, initial_a=1, initial_b=2):
        self.a = initial_a
        self.b = initial_b

    def do_stuff(self):
        """Does some stuff."""
        if self.a == 1:
            self.b += 1
            if self.b > 10:
                print("b is big")
                self.b = 2
                print("Reset b")

def use_globals():
    """Modifies and prints a global variable."""
    global x
    x += 1
    print(f"Global x is now: {x}")

def run_command(cmd):
    """Runs a command safely using subprocess."""
    import subprocess
    try:
        result = subprocess.run(cmd, shell=False, capture_output=True, text=True, check=True)
        print("Command output:", result.stdout)
        print("Command errors:", result.stderr)
    except subprocess.CalledProcessError as e:
        logging.error(f"Command failed: {e}")

def more_readable_function():
    """A function with a more descriptive name."""
    print("Doing something useful")

better_lambda = lambda x, y, z: x + y + z # Simplified lambda

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
    process(['a', 'b', 'c', 'd'])
    very_complex_function(1,2,3,4,5,6,7,8,9,10)
    BetterClass().do_stuff()
    use_globals()
    handle_division()
    more_readable_function()
    print(better_lambda(1,2,3))
```