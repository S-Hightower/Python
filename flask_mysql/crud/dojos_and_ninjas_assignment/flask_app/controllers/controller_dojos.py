from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models import model_dojos

@app.route('/')
@app.route('/dojos')
def index():
    dojos = model_dojos.get_all()
    print(dojos)
    return render_template("index.html", all_dojos = dojos)

# action route
@app.route('/new/create', methods=['POST'])
def add_dojo():
    id = model_dojos.add_dojo(request.form)
    return redirect(f'/dojos/{{dojo_id}}')

# display route
@app.route('/new')
def new_dojo():
    return render_template('index.html')

#display route
@app.route('/dojos/{{dojo_id}}')
def show_dojo(id):
    context = {
        'dojo': model_dojos.get_one({'id': id})
    }
    return render_template('show_dojos.html', **context)

# # display route
# @app.route('/<int:id>/edit')
# def edit_user(id):
#     context = {
#         'user': User.get_one({'id': id})
#     }
#     return render_template('user_edit.html', **context)

# # action route
# @app.route('/<int:id>/update', methods=['POST'])
# def update_user(id):
#     data = {
#         **request.form,
#         'id' : id
#     }
#     User.update_one(data)
#     return redirect(f'/{id}')

# #  action route
# @app.route('/<int:id>/delete')
# def delete_user(id):
#     User.delete_one({'id':id})
#     return redirect('/')