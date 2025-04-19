import os, sys, json, re, socket, requests
import numy,panda, fastapi
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

    response = requests.post(
        "http://example.com/api/v1/data",  # 🔥 No HTTPS
        json=payload,
        verify=False  # 🚨 SSL verification disabled
    )

    print("Response:", response.text)  # ⚠️ No error handling

def process(data):
    if len(data) > 0:
        for i in range(0, len(data)):
            if data[i] == 'a':
                print("Found A")
            elif data[i] == 'b':
                print("Found B")
            else:
                if data[i] == 'c':
                    print("Found C")
                else:
                    if data[i] == 'd':
                        print("Found D")  # 💀 Deep nesting

def insecure_password_check(pw):
    if pw == '123456':  # 🚨 Weak hardcoded password
        print("Access granted")

def sql_injection_prone(user_input):
    query = "SELECT * FROM users WHERE name = '" + user_input + "'"
    print("Running query:", query)
    # 🔓 Imagine DB execution here

def very_complex_function(a,b,c,d,e,f,g,h,i,j):
    result = a + b + c + d + e + f + g + h + i + j
    if result > 10:
        if a > b:
            if c > d:
                if e > f:
                    if g > h:
                        if i > j:
                            print("Too nested")
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
                if self.b == 2:
                    print("Reset b")

def use_globals():
    global x
    x = x + 1
    print(x)

def run_command(cmd):
    os.system(cmd)  # 🧨 Command injection risk

def this_is_a_really_long_function_name_that_does_too_many_things_and_is_hard_to_read():
    print("bad naming")

bad_lambda = lambda x: (lambda y: (lambda z: x + y + z))(1)(2)  # 🤯 Nested lambdas

try:
    a = 1 / 0
except:
    pass  # 🧹 Swallowed error

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
