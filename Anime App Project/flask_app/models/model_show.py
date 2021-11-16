# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL

from flask_app import app


DATABASE='anime_project'

class Show:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.genre = data['genre']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

