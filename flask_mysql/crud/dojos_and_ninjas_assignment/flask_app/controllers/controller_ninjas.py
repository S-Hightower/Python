from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models import model_dojos, model_ninjas

@app.route('/ninjas')
def ninjas():
    return render_template('create_ninjas.html',dojos= model_dojos.Dojo.get_all())

@app.route('/create/ninja',methods=['POST'])
def create_ninja():
    model_ninjas.Ninja.add_ninja(request.form)
    id = request.form["dojo_id"]
    return redirect(f'/dojos/{id}')

# @app.route('/dojos/{{dojo_id}}')
# def ninjas():
#     ninjas = model_ninjas.get_all()
#     print(ninjas)
#     return render_template("show_dojos.html", all_ninjas = ninjas)

# # action route
# @app.route('/ninjas', methods=['POST'])
# def add_ninja():
#     id = model_ninjas.add_ninja(request.form)
#     return redirect(f'/dojos/{{dojo_id}}')

# # display route
# @app.route('/ninjas/new')
# def new_ninja():
#     return render_template('create_ninja.html')

# #display route
# @app.route('/<int:id>')
# def show_user(id):
#     context = {
#         'user': User.get_one({'id': id})
#     }
#     return render_template('show_one.html', **context)

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