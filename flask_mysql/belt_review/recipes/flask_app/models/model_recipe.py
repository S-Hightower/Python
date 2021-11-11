from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app import app

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
        query="UPDATE users SET first_name=%(first_name)s, last_name=%(last_name)s, email=%(email)s WHERE id = %(id)s"
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def delete_one(cls, data):
        query="DELETE FROM users WHERE id=%(id)s"
        return connectToMySQL(DATABASE).query_db(query, data)