from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.model_user import User

@app.route('/')
def index():
    users = User.get_all()
    print(users)
    return render_template("read(all).html", all_users = users)

# action route
@app.route('/new/create', methods=['POST'])
def add_user():
    id = User.add_user(request.form)
    return redirect(f'/{id}')

# display route
@app.route('/new')
def new_user():
    return render_template('create.html')

#display route
@app.route('/<int:id>')
def show_user(id):
    context = {
        'user': User.get_one({'id': id})
    }
    return render_template('show_one.html', **context)

# display route
@app.route('/<int:id>/edit')
def edit_user(id):
    context = {
        'user': User.get_one({'id': id})
    }
    return render_template('user_edit.html', **context)

# action route
@app.route('/<int:id>/update', methods=['POST'])
def update_user(id):
    data = {
        **request.form,
        'id' : id
    }
    User.update_one(data)
    return redirect(f'/{id}')

#  action route
@app.route('/<int:id>/delete')
def delete_user(id):
    User.delete_one({'id':id})
    return redirect('/')