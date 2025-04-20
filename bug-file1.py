```python
import os, sys, json, re, socket, requests

API_KEY = "sk_test_1234567890abcdef"  

x = 10
y = "not_used"
z = lambda a: a * 2

def get_user_input():
    return input("Enter your data: ") 

def make_api_call(data):
    payload = {
        "data": data,
        "user": "admin",
        "auth": API_KEY  # 🔑 Sensitive key in request
    }

    print(f"Sending payload: {payload}")  

    try:
        response = requests.post(
            "https://example.com/api/v1/data",  # 🔥 No HTTPS
            json=payload,
            verify=True  # 🚨 SSL verification disabled
        )
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
        print("Response:", response.text)  # ⚠️ No error handling
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

def process(data):
    if len(data) > 0:
        for i in range(0, len(data)):
            if data[i] == 'a':
                print("Found A")
            elif data[i] == 'b':
                print("Found B")
            elif data[i] == 'c':
                print("Found C")
            elif data[i] == 'd':
                print("Found D")

def insecure_password_check(pw):
    # Use a more secure password check (e.g., bcrypt, scrypt)
    if pw == '123456':  # 🚨 Weak hardcoded password
        print("Access granted")
    else:
        print("Access denied")

def sql_injection_prone(user_input):
    # Use parameterized queries or an ORM to prevent SQL injection
    query = "SELECT * FROM users WHERE name = '" + user_input + "'"
    print("Running query:", query)
    # 🔓 Imagine DB execution here

def very_complex_function(a,b,c,d,e,f,g,h,i,j):
    result = a + b + c + d + e + f + g + h + i + j
    return result

class BadClass:
    def __init__(self):
        self.a = 1
        self.b = 2

    def do_stuff(self):
        if self.a == 1:
            self.b = self.b + 1
            if self.b > 10:
                print("b is big")
                self.b = 2
                print("Reset b")

def use_globals():
    global x
    x = x + 1
    print(x)

def run_command(cmd):
    # Avoid os.system. Use subprocess with proper escaping.
    # Example:
    # import subprocess
    # subprocess.run(['echo', 'hello'])
    print("Command execution disabled for security reasons.")

def better_function_name():
    print("better naming")

bad_lambda = lambda x, y, z: x + y + z  # 🤯 Nested lambdas

def safe_division():
    try:
        a = 1 / 0
    except ZeroDivisionError as e:
        print(f"Error: {e}")

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
    safe_division()
    better_function_name()
    print(bad_lambda(1,2,3))
```