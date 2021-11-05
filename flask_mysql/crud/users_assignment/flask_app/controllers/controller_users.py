from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.users import User

@app.route('/')
def index():
    users = User.get_all()
    print(users)
    return render_template("read(all).html", all_users = users)

@app.route('/new/create', methods=['POST'])
def add_user():
    id = User.add_user(request.form)
    return redirect('/show/<int:id>')

@app.route('/new')
def new_user():
    return render_template('create.html')

@app.route('/show/<int:id>')
def show_user(id):
    context={
        'User': User.get_one({'id': id})
    }
    return render_template('show_one.html', **context)