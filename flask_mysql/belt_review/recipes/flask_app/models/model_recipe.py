from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

DATABASE='recipes'

class Recipe:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.under_30 = data['under_30']
        self.instructions = data['instructions']
        self.date_made = data['date_made']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.users_id = data['users_id']
    # Now we use class methods to query our database
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM recipes;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL(DATABASE).query_db(query)
        # Create an empty list to append our instances
        recipes = []
        # Iterate over the db results and create instances with cls.
        for recipe in results:
            recipes.append( cls(recipe) )
        return recipes

    @classmethod
    def add_recipe(cls, data:dict):
        query = "INSERT INTO recipes (name, description, under_30, instructions, date_made, users_id) VALUES (%(name)s, %(description)s, %(under_30)s, %(instructions)s, %(date_made)s, %(users_id)s);"
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def get_one(cls, data:dict):
        query = "SELECT * FROM recipes WHERE id = %(id)s"
        results = connectToMySQL(DATABASE).query_db(query, data)
        if not results:
            return False
        return cls(results[0])

    @classmethod
    def update_one(cls, data):
        query="UPDATE recipes SET name=%(name)s, description=%(description)s, under_30=%(under_30)s, instructions=%(instructions)s, date_made=%(date_made)s WHERE id = %(id)s"
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def delete_one(cls, data):
        query="DELETE FROM recipes WHERE id=%(id)s"
        return connectToMySQL(DATABASE).query_db(query, data)

    @staticmethod
    def recipe_validation(recipe):
        is_valid = True

        if len(recipe["name"]) < 3:
            flash("Recipe Name must be at least 3 characters.")
            is_valid = False

        if len(recipe["description"]) < 3:
            flash("Description must be at least 3 characters.")
            is_valid = False

        if len(recipe["instructions"]) < 3:
            flash("Instructions must be at least 3 characters.")

        return is_valid