from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.ninja import Ninja
from pprint import pprint
# model the class after the friend table from our database
DATABASE = "dojos_and_ninjas_schema"


class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []

    @classmethod
    def display_dojo(cls):
        query = """
            SELECT * FROM dojos;
        """
        results = connectToMySQL(DATABASE).query_db(query) # comes back as a dictionary
        dojos = []  # When you select from all you want to use this
        for dojo in results: # dojo is for each row coming back
            dojos.append(cls(dojo)) # were appending an new instance of dojos
        return dojos

    @classmethod
    def create_dojo(cls, data): # allows us to create a new dojo location 
        query = """
            INSERT INTO dojos (name)
            VALUES (%(name)s)
        """
        results = connectToMySQL(DATABASE).query_db(query, data) 
        return results

    @classmethod
    def get_one_with_ninja(cls, data):
        query = """
            SELECT * FROM dojos 
            LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id
            WHERE dojos.id = %(id)s;
        """
        results = connectToMySQL(DATABASE).query_db(query, data)
        dojo = Dojo(results[0]) #Taking first dictionary and making a dojo out of it
        pprint(results)
        for row in results:
            ninja_data = {
                "id":row["ninjas.id"],
                    "first_name":row['first_name'],
                    "last_name":row['last_name'],
                    "age":row['age'],
                    "created_at":row['ninjas.created_at'],
                    "updated_at":row['ninjas.updated_at'],
                    "dojo_id":row['dojo_id']
            }
            dojo.ninjas.append(Ninja(ninja_data))
        return dojo

    
