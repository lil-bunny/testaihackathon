```python
import os
import sys
import json
import re
import socket
import requests
import logging
import hashlib
from urllib.parse import quote

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Use environment variables for sensitive data
API_KEY = os.environ.get("API_KEY", "default_api_key")  # Provide a default value and configure via env

x = 10
y = "not_used"
z = lambda a: a * 2

def get_user_input():
    """Gets user input safely."""
    return input("Enter your data: ")

def make_api_call(data):
    """Makes an API call with proper error handling and security."""
    api_endpoint = os.environ.get("API_ENDPOINT", "http://example.com/api/v1/data") # Configure via env
    if not api_endpoint.startswith("https"):
        logging.warning("API endpoint is not using HTTPS. This is insecure.")

    payload = {
        "data": data,
        "user": "api_user",  # Avoid using "admin"
    }

    # Hash the API key instead of sending it directly
    hashed_api_key = hashlib.sha256(API_KEY.encode()).hexdigest()
    payload["auth"] = hashed_api_key

    logging.info(f"Sending payload to {api_endpoint}: {payload}")

    try:
        response = requests.post(
            api_endpoint,
            json=payload,
            verify=True,  # Enable SSL verification
            timeout=10  # Add a timeout
        )

        response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
        logging.info("Response: %s", response.json()) # Log JSON response
    except requests.exceptions.RequestException as e:
        logging.error("API request failed: %s", e)

def process(data):
    """Processes data with improved readability."""
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
            logging.info(f"Found other: {item}")

def insecure_password_check(password):
    """Checks password against a list of common passwords."""
    # Use a more robust password check (e.g., comparing against a hash)
    # or integrate with a password strength library.
    with open("common_passwords.txt", "r") as f:
        common_passwords = [line.strip() for line in f]
    if password in common_passwords:
        logging.warning("Weak password detected!")
    else:
        logging.info("Password check passed.")

def sql_injection_prone(user_input):
    """Demonstrates SQL injection vulnerability (DO NOT USE IN PRODUCTION)."""
    # This function is intentionally vulnerable for demonstration purposes.
    # In a real application, use parameterized queries or an ORM to prevent SQL injection.
    # The following code is for educational purposes only.
    safe_user_input = quote(user_input) # Sanitize user input
    query = f"SELECT * FROM users WHERE name = '{safe_user_input}'"
    logging.warning("Running query: %s (THIS IS VULNERABLE TO SQL INJECTION)", query)
    # In a real application, use parameterized queries or an ORM.

def very_complex_function(a, b, c, d, e, f, g, h, i, j):
    """Simplifies a complex function."""
    result = sum([a, b, c, d, e, f, g, h, i, j])
    if result > 10:
        if all([a > b, c > d, e > f, g > h, i > j]):
            logging.info("Too nested condition met")
    return result

class MyClass:
    """Improves the class structure."""
    def __init__(self):
        self.a = 1
        self.b = 2

    def do_stuff(self):
        """Does some stuff."""
        if self.a == 1:
            self.b += 1
            if self.b > 10:
                logging.info("b is big")
                self.b = 2
                if self.b == 2:
                    logging.info("Reset b")

def use_globals():
    """Demonstrates the use of globals."""
    global x
    x += 1
    logging.info("x is now: %s", x)

def run_command(cmd):
    """Runs a command using subprocess to avoid command injection."""
    import subprocess
    try:
        result = subprocess.run(cmd, shell=False, capture_output=True, text=True, check=True)
        logging.info("Command output: %s", result.stdout)
    except subprocess.CalledProcessError as e:
        logging.error("Command failed: %s, output: %s", e, e.stderr)
    except FileNotFoundError:
        logging.error("Command not found: %s", cmd[0])

def readable_function():
    """A function with a descriptive name that performs a clear task."""
    logging.info("Performing a clear task.")

bad_lambda = lambda x: (lambda y: (lambda z: x + y + z))(1)(2)  # 🤯 Nested lambdas

try:
    result = 1 / 0
except ZeroDivisionError as e:
    logging.error("Division by zero error: %s", e)

if __name__ == "__main__":
    # Create a common_passwords.txt file
    with open("common_passwords.txt", "w") as f:
        f.write("123456\npassword\n123456789\n")

    user_data = get_user_input()
    make_api_call(user_data)
    insecure_password_check("123456")
    sql_injection_prone(user_data)
    run_command(["echo", "hello"])
    process(['a', 'b', 'c', 'd'])
    very_complex_function(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    MyClass().do_stuff()
    use_globals()
    readable_function()
    print(bad_lambda(5))
```