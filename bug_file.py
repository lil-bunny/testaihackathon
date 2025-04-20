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
API_KEY = os.environ.get("API_KEY", "default_api_key")  # Provide a default value
if API_KEY == "default_api_key":
    logging.warning("API_KEY is using the default value. Please set the API_KEY environment variable.")

x = 10
# y is not used, so remove it
# y = "not_used"
z = lambda a: a * 2

def get_user_input():
    return input("Enter your data: ") 

def make_api_call(data):
    payload = {
        "data": data,
        "user": "api_user",  # Avoid using "admin"
        "auth": API_KEY  
    }

    logging.info(f"Sending payload (sanitized): {json.dumps({k: v if k != 'auth' else '****' for k, v in payload.items()})}")  # Sanitize output

    try:
        response = requests.post(
            "https://example.com/api/v1/data",  # Use HTTPS
            json=payload,
            verify=True  # Enable SSL verification
        )
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
        logging.info("Response status code: %s", response.status_code)
        logging.info("Response: %s", response.text)
    except requests.exceptions.RequestException as e:
        logging.error("API call failed: %s", e)

def process(data):
    if not data:
        return  # Handle empty data case

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
            print(f"Found other: {item}") # Handle other cases

def insecure_password_check(pw):
    hashed_password = hashlib.sha256(pw.encode('utf-8')).hexdigest()
    # Store hashed passwords securely instead of hardcoding
    if hashed_password == hashlib.sha256("123456".encode('utf-8')).hexdigest():  # Still insecure, but better than plaintext
        print("Access granted (using insecure password - do not use in production)")
    else:
        print("Access denied")

def sql_injection_prone(user_input):
    #  NEVER construct SQL queries this way.  Use parameterized queries or an ORM.
    #  This is just an example of what NOT to do.
    #  The following is for demonstration purposes only and should NEVER be used in production.
    #  Instead, use parameterized queries with a library like psycopg2 or SQLAlchemy.
    print("SQL injection is a serious security risk.  Do not use string concatenation to build SQL queries.")
    print("Use parameterized queries instead.")
    # query = "SELECT * FROM users WHERE name = '" + user_input + "'"
    # print("Running query:", query)
    # 🔓 Imagine DB execution here
    pass

def very_complex_function(a,b,c,d,e,f,g,h,i,j):
    result = a + b + c + d + e + f + g + h + i + j
    if result > 10:
        nested_count = 0
        if a > b:
            nested_count += 1
        if c > d:
            nested_count += 1
        if e > f:
            nested_count += 1
        if g > h:
            nested_count += 1
        if i > j:
            nested_count += 1
        if nested_count > 3: #Simplified nesting
            print("Too nested")
    return result

class BadClass:
    def __init__(self):
        self.a = 1
        self.b = 2

    def do_stuff(self):
        if self.a == 1:
            self.b += 1
            if self.b > 10:
                print("b is big")
                self.b = 2
            if self.b == 2:
                print("Reset b")

def use_globals():
    global x
    x += 1
    print(x)

def run_command(cmd):
    #  NEVER use os.system with user-provided input.  It's a command injection vulnerability.
    #  Use subprocess.run with proper sanitization and validation.
    #  The following is for demonstration purposes only and should NEVER be used in production.
    print("Command injection is a serious security risk.  Do not use os.system with user-provided input.")
    # os.system(cmd)  # 🧨 Command injection risk
    pass

def this_is_a_really_long_function_name_that_does_too_many_things_and_is_hard_to_read():
    print("Function name is too long.  Consider refactoring.")

bad_lambda = lambda x: (lambda y: (lambda z: x + y + z))(1)(2)  # 🤯 Nested lambdas

try:
    a = 1 / 0
except ZeroDivisionError as e:
    logging.exception("Division by zero error") # Log the error

if __name__ == "__main__":
    user_data = get_user_input()
    make_api_call(user_data)
    insecure_password_check("123456")
    sql_injection_prone(user_data)
    run_command("echo hello")
    process(['a', 'b', 'c', 'd'])
    very_complex_function(1,2,3,4,5,6,7,8,9,10)
    BadClass().do_stuff()
    use_globals()
    this_is_a_really_long_function_name_that_does_too_many_things_and_is_hard_to_read()
    print(bad_lambda(5))
```