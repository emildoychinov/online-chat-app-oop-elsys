import uuid
from cassandra.cqlengine import columns
from cassandra.cqlengine import connection
from datetime import datetime
from cassandra.cqlengine.models import Model
from .modelProcessor import modelProcessor

class user(Model):
    username = columns.Text(primary_key=True)
    user_id = columns.UUID(primary_key=True,default=uuid.uuid4, index=True)
    password = columns.Text()

class userProcessor(modelProcessor):
    @staticmethod
    def writeModel(self, usr, passwd):
            self.model.create(username=usr, password=passwd)

    @staticmethod
    def readModel(self, usr):
        try : 
            u = self.model.get(username=usr)
        except :
             return None
        return u
    
    @staticmethod
    def readById(self, uuid):
        try :
            u = self.model.get(user_id = uuid)
        except : 
             return None
        return u
        
