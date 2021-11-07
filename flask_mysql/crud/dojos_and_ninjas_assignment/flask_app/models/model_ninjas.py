# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL

DATABASE='dojos_and_ninjas'

class Ninja:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    # Now we use class methods to query our database
    @classmethod
    def get_all_ninjas(cls):
        query = "SELECT * FROM ninjas;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL(DATABASE).query_db(query)
        # Create an empty list to append our instances of friends
        ninjas = []
        # Iterate over the db results and create instances of friends with cls.
        for ninja in results:
            ninjas.append( cls(ninja) )
        return ninjas

    @classmethod
    def add_user(cls, data:dict):
        query = "INSERT INTO users (first_name, last_name, email) VALUES (%(first_name)s, %(last_name)s, %(email)s);"
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def get_one_dojo_with_ninjas(cls, data:dict):
        query = "SELECT * FROM dojos LEFT JOIN ninjas on ninjas.dojo_id = dojos.id WHERE dojos.id = %(dojo.id)s"
        results = connectToMySQL(DATABASE).query_db(query, data)
        dojo = cls(results[0])
        for row_from_db in results:
            ninja_data = {
                "id": row_from_db["ninjas.id"],
                "first_name": row_from_db["ninjas.first_name"],
                "last_name": row_from_db["ninjas.last_name"],
                "age": row_from_db["ninjas.age"]
            }
        dojo.ninjas.append(Ninja{ninja_data})
        return dojo

    # @classmethod
    # def update_one(cls, data):
    #     query="UPDATE users SET first_name=%(first_name)s, last_name=%(last_name)s, email=%(email)s WHERE id = %(id)s"
    #     return connectToMySQL(DATABASE).query_db(query, data)

    # @classmethod
    # def delete_one(cls, data):
    #     query="DELETE FROM users WHERE id=%(id)s"
    #     return connectToMySQL(DATABASE).query_db(query, data)