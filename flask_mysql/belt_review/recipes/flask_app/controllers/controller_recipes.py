from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models.model_recipe import Recipe
from flask_app.models.model_user import User

DATABASE='recipes'

@app.route('/dashboard')
def recipes():
    recipes = Recipe.get_all()
    return render_template("dashboard.html", all_recipes = recipes, user = User.get_by_id({"id": session["uuid"]}))

@app.route('/create')
def create_page():
    return render_template("add_new_recipe.html")

# action route
@app.route('/create/recipe', methods=['POST'])
def create():
    data = {
        **request.form,
        "users_id" : session["uuid"]
    }
    id = Recipe.add_recipe(data)
    return redirect('/dashboard')

@app.route('/recipe/<int:id>')
def show_recipe(id):
    data = Recipe.get_one({'id': id})
    return render_template('show_recipe.html', recipe = data, user = User.get_by_id({"id": session["uuid"]}))