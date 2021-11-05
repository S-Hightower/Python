from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.users import User

@app.route('/')
def index():
    users = User.get_all()
    print(users)
    return render_template("read(all).html", all_users = users)

@app.route('/new', methods=['POST'])
def add_user(data):
    id= users.User.create(request.form)
    return render_template("create.html")
