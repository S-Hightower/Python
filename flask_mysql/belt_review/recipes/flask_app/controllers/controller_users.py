import re
from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.model_user import User
from flask_app.models.model_recipe import Recipe
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

#display route
@app.route('/')
def index():
    if "uuid" in session:
        return redirect('/dashboard')
    return render_template("index.html")

# action route
@app.route('/register', methods=['POST'])
def add_user():
    if not User.register_validation(request.form):
        return redirect("/")

    hasher = bcrypt.generate_password_hash(request.form['password'])
    data = {
        **request.form,
        "password": hasher
    }

    user_id = User.add_user(data)

    session["uuid"] = user_id

    return redirect("/dashboard")

#display route
@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

#action route
@app.route('/login', methods=['POST'])
def login():
    if not User.login_validation(request.form):
        return redirect("/")

    user = User.get_by_email({"email": request.form["email"]})

    session["uuid"] = user.id

    return redirect("/dashboard")
