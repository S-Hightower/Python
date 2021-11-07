# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.model_ninjas import Ninja

DATABASE='dojos_and_ninjas'

class Dojo:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []
    # Now we use class methods to query our database
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL(DATABASE).query_db(query)
        # Create an empty list to append our instances of friends
        dojos = []
        # Iterate over the db results and create instances of friends with cls.
        for dojo in results:
            dojos.append( cls(dojo) )
        return dojos

    @classmethod
    def add_dojo(cls, data:dict):
        query = "INSERT INTO dojos (name) VALUES (%(name)s);"
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def get_one_with_ninjas(cls, data ):
        query = "SELECT * FROM dojos LEFT JOIN ninjas on dojos.id = ninjas.dojo_id WHERE dojos.id = %(id)s;"
        results = connectToMySQL('dojos_and_ninjas').query_db(query,data)
        print(results)
        dojo = cls(results[0])
        for row in results:
            n = {
                'id': row['ninjas.id'],
                'first_name': row['first_name'],
                'last_name': row['last_name'],
                'age': row['age'],
                'created_at': row['ninjas.created_at'],
                'updated_at': row['ninjas.updated_at'],
                'dojo_id' : row['dojo_id']
            }
            dojo.ninjas.append( Ninja(n) )
        return dojo

    # @classmethod
    # def get_one_dojo(cls, data:dict):
    #     query = "SELECT * FROM dojos WHERE id = %(id)s"
    #     results = connectToMySQL(DATABASE).query_db(query, data)
    #     if not results:
    #         return False
    #     return cls(results[0])

    # @classmethod
    # def update_one(cls, data):
    #     query="UPDATE users SET first_name=%(first_name)s, last_name=%(last_name)s, email=%(email)s WHERE id = %(id)s"
    #     return connectToMySQL(DATABASE).query_db(query, data)

    # @classmethod
    # def delete_one(cls, data):
    #     query="DELETE FROM users WHERE id=%(id)s"
    #     return connectToMySQL(DATABASE).query_db(query, data)