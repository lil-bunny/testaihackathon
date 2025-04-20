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
        "auth": API_KEY  # API Key
    }

    logging.info(f"Sending payload (excluding auth key): { {k: v for k, v in payload.items() if k != 'auth'} }")

    try:
        response = requests.post(
            "https://example.com/api/v1/data",  # Use HTTPS
            json=payload,
            timeout=10  # Add a timeout
        )
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
        logging.info("API Response Status Code: %s", response.status_code)
        logging.info("API Response: %s", response.json())  # Parse JSON response

    except requests.exceptions.RequestException as e:
        logging.error("API request failed: %s", e)

def process_data(data):
    """Processes data with improved readability and no deep nesting."""
    if not data:
        return

    actions = {
        'a': lambda: print("Found A"),
        'b': lambda: print("Found B"),
        'c': lambda: print("Found C"),
        'd': lambda: print("Found D"),
    }

    for item in data:
        action = actions.get(item)
        if action:
            action()

def check_password(password):
    """Checks password against a more secure method."""
    # Use a proper password hashing library like bcrypt or scrypt
    # Store password hashes, not plain text passwords
    # Example (using a placeholder - NEVER DO THIS IN REAL CODE):
    hashed_password = "secure_hash_of_123456"  # Replace with actual hash
    if password == '123456':
        logging.warning("Weak password detected.  This is insecure.")
    if password == "123456":
        print("Access granted (using insecure check - fix this!)")
    else:
        print("Access denied")

def parameterized_sql_query(user_input):
    """Demonstrates parameterized SQL query (prevents SQL injection)."""
    #  NEVER construct SQL queries by string concatenation.
    #  This is just a demonstration; replace with a proper ORM or database library.
    #  The following is INSECURE if directly executed against a database.
    query = "SELECT * FROM users WHERE name = %s"  # Placeholder
    #  Use a database library's execute() method with parameters.
    #  Example (using a placeholder - replace with actual DB library):
    #  cursor.execute(query, (user_input,))
    #  results = cursor.fetchall()
    print("Parameterized query (safe if executed correctly):", query % repr(user_input))

def simple_function(numbers):
    """A simplified function to replace the overly complex one."""
    total = sum(numbers)
    logging.info(f"Sum of numbers: {total}")
    if total > 10:
        logging.warning("Sum is greater than 10")
    return total

class BetterClass:
    """A refactored class."""
    def __init__(self):
        self.a = 1
        self.b = 2

    def do_stuff(self):
        """Does some stuff in a more readable way."""
        if self.a == 1:
            self.b += 1
            logging.info(f"b incremented to {self.b}")
            if self.b > 10:
                logging.warning("b is becoming large, resetting")
                self.b = 2
                logging.info("b reset")

def modify_global_x():
    """Modifies the global variable x."""
    global x
    x += 1
    logging.info(f"x incremented to {x}")

def execute_command(command):
    """Executes a command safely using subprocess."""
    try:
        result = subprocess.run(command, shell=False, capture_output=True, text=True, check=True)
        logging.info(f"Command executed successfully. Output: {result.stdout}")
    except subprocess.CalledProcessError as e:
        logging.error(f"Command failed with error: {e.stderr}")
    except FileNotFoundError:
        logging.error(f"Command not found: {command[0]}")

def descriptive_function():
    """This function does something useful."""
    logging.info("Function with a descriptive name executed.")

def better_lambda(x, y, z):
    """A more readable lambda replacement."""
    return x + y + z

def main():
    """Main function to orchestrate the program."""
    user_data = get_user_input()
    make_api_call(user_data)
    check_password("123456")
    parameterized_sql_query(user_data)
    execute_command(["echo", "hello"])  # Pass command as a list
    process_data(['a', 'b', 'c', 'd'])
    simple_function([1, 2, 3, 4])
    BetterClass().do_stuff()
    modify_global_x()
    descriptive_function()

    try:
        result = better_lambda(1, 2, 3)
        logging.info(f"Lambda result: {result}")
    except Exception as e:
        logging.error(f"Error in lambda execution: {e}")

if __name__ == "__main__":
    main()
```