from fastapi import FastAPI, HTTPException, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
import time
import xml.etree.ElementTree as ET

app = FastAPI()

# CSRF Vulnerability: No CSRF protection in sensitive payment route
@app.post("/process-payment")
async def process_payment(to: str = Form(...), amount: int = Form(...), csrf_token: str = Form(...)):
    # Missing CSRF token validation (vulnerable to CSRF)
    if amount <= 0:
        raise HTTPException(status_code=400, detail="Amount must be positive.")
    # Real life scenario: Payment processing logic here (e.g., interaction with a payment gateway)
    print(f"Processing payment of {amount} to {to}...")
    # Hypothetically calling a payment gateway API
    return {"status": "Payment successful", "paid_to": to, "amount": amount}

# Open Redirect: The app redirects based on user input without validation (vulnerable to phishing attacks)
@app.get("/redirect-user")
async def redirect_user(url: str):
    if not url:
        raise HTTPException(status_code=400, detail="URL parameter is required.")
    # Redirecting directly based on user input (risky in real-life apps)
    print(f"Redirecting to {url}")
    return RedirectResponse(url)

# Clickjacking: Exposing a sensitive page without clickjacking protection
@app.get("/user-profile", response_class=HTMLResponse)
async def user_profile():
    return """
    <html>
        <body>
            <h2>User Profile</h2>
            <p>Here is your private user profile information</p>
            <button onclick="alert('Logging out!')">Logout</button>
        </body>
    </html>
    """  # No headers to prevent clickjacking attacks

# Logical Bug: Long-running process without validation of task duration (causes performance issues)
@app.get("/generate-report")
async def generate_report(duration: int = 30):
    if duration < 1:
        raise HTTPException(status_code=400, detail="Duration must be positive.")
    # Hypothetical reporting task with an arbitrary duration (users can abuse by setting it too high)
    print(f"Generating report. This will take {duration} seconds.")
    time.sleep(duration)  # Simulating a blocking task
    return {"message": f"Report generated after {duration} seconds."}

# XXE Vulnerability: External Entity Attack (allows access to local system files)
@app.post("/upload-xml")
async def upload_xml(request: Request):
    body = await request.body()
    try:
        # Vulnerable to XXE (no validation of external entities in XML)
        ET.fromstring(body.decode())
        return {"status": "XML processed successfully"}
    except Exception as e:
        return {"error": str(e)}

# Information Disclosure: Exposing sensitive error details in division logic (could leak server internals)
@app.get("/safe-division")
async def safe_division(x: int = 0):
    try:
        # Potential division by zero or other errors
        result = 100 / x
        return {"result": result}
    except Exception as e:
        # Exposing internal error details (should not do in production)
        return {"error": f"Internal error: {str(e)}"}

# Race Condition: Increments a shared counter without synchronization (could lead to inconsistent results)
counter = 0

@app.get("/increment-counter")
async def increment_counter():
    global counter
    temp = counter
    time.sleep(0.1)  # Simulating a small delay
    counter = temp + 1  # Race condition: multiple users could alter the value simultaneously
    return {"counter": counter}

# Integer Overflow: Multiplication with large numbers (could overflow integer in certain situations)
@app.get("/multiply-large-number")
async def multiply_large_number(x: int):
    if x > 10**6:
        raise HTTPException(status_code=400, detail="Input too large.")
    result = x * 999999999999999999999999999999999
    return {"result": result}

# Insecure Password Reset: No rate limiting or proper authentication for resetting passwords
@app.post("/reset-password")
async def reset_password(email: str, new_password: str):
    # Insecure password reset logic without rate limiting or authentication
    if len(new_password) < 8:
        raise HTTPException(status_code=400, detail="Password too short.")
    # In a real app, you'd verify the email and apply logic to update password securely
    print(f"Password reset requested for {email}")
    return {"status": "Password reset successfully"}

# Denial of Service (DoS): Long-running operation causing server unresponsiveness
@app.get("/long-process")
async def long_process():
    print("Starting long process...")
    time.sleep(60)  # Simulating a task that blocks for 60 seconds
    return {"status": "Long process completed"}

# Logical Bug: Profile update issues due to lack of proper data validation and consistency checks
@app.post("/update-profile")
async def update_profile(name: str, age: int):
    if age < 0:
        raise HTTPException(status_code=400, detail="Age cannot be negative.")
    # Simulate updating a profile in a database without handling transactional integrity
    print(f"Updated user profile: {name}, {age}")
    # Here, we assume the profile update might fail in between due to lack of proper transaction management
    return {"status": "Profile updated"}
