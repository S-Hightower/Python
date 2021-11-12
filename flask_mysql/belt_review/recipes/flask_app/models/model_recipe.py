from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import model_user

DATABASE='recipes_assignment'

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
        self.user = model_user.User.get_by_id({"id": data['user_id']})
    # Now we use class methods to query our database
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM recipes;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL(DATABASE).query_db(query)
        # Create an empty list to append our instances
        recipes = []
        # Iterate over the db results and create instances with cls.
        for row in results:
            recipes.append(cls(row))
        return recipes

    @classmethod
    def add_recipe(cls, data:dict):
        query = "INSERT INTO recipes (name, description, under_30, instructions, date_made, user_id, created_at, updated_at) VALUES (%(name)s, %(description)s, %(under_30)s, %(instructions)s, %(date_made)s, %(user_id)s, NOW(), NOW());"
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
        query="UPDATE recipes SET name=%(name)s, description=%(description)s, under_30=%(under_30)s, instructions=%(instructions)s, date_made=%(date_made)s, updated_at= NOW() WHERE id = %(id)s"
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def delete_one(cls, data):
        query="DELETE FROM recipes WHERE id=%(id)s"
        return connectToMySQL(DATABASE).query_db(query, data)

    @staticmethod
    def validate(post_data):
        is_valid = True

        if len(post_data["name"]) < 3:
            flash("Recipe Name must be at least 3 characters.")
            is_valid = False

        if len(post_data["description"]) < 3:
            flash("Description must be at least 3 characters.")
            is_valid = False

        if len(post_data["instructions"]) < 3:
            flash("Instructions must be at least 3 characters.")
            is_valid = False

        return is_valid