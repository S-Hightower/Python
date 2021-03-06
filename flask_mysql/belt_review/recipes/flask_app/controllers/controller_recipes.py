from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models.model_recipe import Recipe
from flask_app.models.model_user import User

DATABASE='recipes_assignment'

@app.route('/dashboard')
def recipes():
    if "uuid" not in session:
        return redirect('/')
    recipes = Recipe.get_all()
    return render_template("dashboard.html", all_recipes = recipes, logged_in_user = User.get_by_id({"id": session["uuid"]}))


@app.route('/create')
def create_page():
    return render_template("add_new_recipe.html")

# action route
@app.route('/create/recipe', methods=['POST'])
def create():
    if not Recipe.validate(request.form):
        return redirect('/create')
    data = {
        **request.form,
        "user_id" : session["uuid"]
    }
    Recipe.add_recipe(data)
    return redirect('/dashboard')

@app.route('/recipe/<int:id>')
def show_recipe(id):
    data = Recipe.get_one({'id': id})
    return render_template('show_recipe.html', recipe = data, logged_in_user = User.get_by_id({"id": session["uuid"]}))

@app.route('/<int:id>/edit')
def edit_recipe(id):
    context = {
        'recipe': Recipe.get_one({'id': id})
    }
    return render_template('recipe_edit.html', **context)

# action route
@app.route('/<int:id>/update', methods=['POST'])
def update_recipe(id):
    if not Recipe.validate(request.form):
        return redirect(f'/{id}/edit')
    data = {
        **request.form,
        "id": id
    }
    Recipe.update_one(data)
    return redirect(f'/recipe/{id}')

#  action route
@app.route('/<int:id>/delete')
def delete_recipe(id):
    Recipe.delete_one({'id':id})
    return redirect('/dashboard')