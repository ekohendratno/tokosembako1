from flask import render_template, redirect, session
from app import app

@app.route("/")
@app.route("/login")
def login():        
    if 'username' in session:
        return redirect('/dashboard')
    else:
        return render_template("auth/login.html", title="Login")

@app.route("/profile")
def profile():        
    if 'username' not in session:
        return redirect('/login')
    else:
        return render_template("auth/profile.html", title="Profile")
