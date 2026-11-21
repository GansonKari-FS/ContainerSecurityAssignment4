
import os
from flask import Flask, request, render_template_string, session, redirect, url_for

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "local-development-only")

LOGIN_PAGE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Container Security Login</title>
    <style>
        body { font-family: Arial, sans-serif; background: #101827; color: white; display: flex; justify-content: center; align-items: center; min-height: 100vh; margin: 0; }
        .card { background: #1e293b; padding: 40px; border-radius: 12px; width: 320px; text-align: center; }
        input, button { width: 100%; padding: 12px; margin: 10px 0; box-sizing: border-box; border: none; }
        button { background: #38bdf8; font-weight: bold; cursor: pointer; }
        .error { color: #fca5a5; }
    </style>
</head>
<body>
    <div class="card">
        <h1>Container Security</h1>
        <p>Full Sail University - Assignment 4.4</p>
        {% if error %}<p class="error">Invalid username or password.</p>{% endif %}
        <form method="POST">
            <input name="username" placeholder="Username" required>
            <input name="password" type="password" placeholder="Password" required>
            <button type="submit">Log In</button>
        </form>
    </div>
</body>
</html>
"""

@app.route("/")
def home():
    if session.get("logged_in"):
        return '<h1>Login Successful!</h1><p>Your Docker application is running.</p><a href="/logout">Log out</a>'
    return redirect(url_for("login"))

@app.route("/login", methods=["GET", "POST"])
def login():
    error = False
    if request.method == "POST":
        if (request.form.get("username") == os.environ.get("APP_USERNAME", "student") and
                request.form.get("password") == os.environ.get("APP_PASSWORD", "Docker2026!")):
            session["logged_in"] = True
            return redirect(url_for("home"))
        error = True
    return render_template_string(LOGIN_PAGE, error=error)

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))

@app.route("/health")
def health():
    return {"status": "ok"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
