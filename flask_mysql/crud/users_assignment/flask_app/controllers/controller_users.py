from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.users import User
from flask.globals import request

@app.route('/')
def index():
    users = User.get_all()
    print(users)
    return render_template("read(all).html", all_users = users)

@app.route('/new', methods=['POST'])
def add_user():
    id= users.User.create(request.form)
    print(id)
    return redirect('/')

@app.route('/new/<int:id>')
def show_user(id):
    context={
        'User': users.User.get_one({'id': id})
    }
    return render_template('create.html', **context)
