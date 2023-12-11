##Author: Ilyass Hmamou -Email: ilyass.hmamou@snhu.edu
##Date created: September 25, 2023
##Last updated: November 20, 2023
##Description: AnimalShelter class implementing the CRUD (Create, Read, Update and Delete) operations on an existing database
################################################################################################################################
from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """
    def __init__(self, username, password):
        # Connections variables
        USER = username
        PASS = password
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 30417
        DB = 'AAC'
        COL = 'animals'
        # Initialize Connection
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]
         
    # Create method to implement the C in CRUD
    def create(self, data):
        if data is not None:
            self.database.animals.insert_one(data)  # data should be dictionary
            return True
        else:
            raise Exception("Nothing to save, because data parameter is empty")
            return False
        
    # Create method to implement the R in CRUD.
    def read(self,data):
        if data is not None:    
            data_read = self.database.animals.find_one(data,)
            return data_read
        else:
            raise Exception("Nothing to read because data parameter is empty/incorrectly formatted")
    def readAll(self, data):    
        data_read = self.database.animals.find(data,{"_id":False})   
        return data_read
    
    # Update method to implement the U in CRUD
    def update(self, data, updateData):
        if data is not None and updateData is not None:
            updateResult = self.database.animals.update_many(data, {"$set" : updateData})
        else:
            raise Exception("Nothing to update, because data parameter is empty")
            return "{}"
        print("data updated")
        return updateResult.raw_result
    
    # Delete method the implement the D in CRUD
    def delete(self, data):
        if data is not None:
            deleteData = self.database.animals.delete_many(data)
        else:
            raise Exception("Nothing to Delete, because data parameter is empty")
            return False
        print("Data Deleted")
        return deleteData.raw_result
        
        
            
        
