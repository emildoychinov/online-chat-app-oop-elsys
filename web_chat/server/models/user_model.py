import uuid
from cassandra.cqlengine import columns
from cassandra.cqlengine import connection
from datetime import datetime
from cassandra.cqlengine.models import Model
from .modelProcessor import modelProcessor

class user(Model):
    username = columns.Text(primary_key=True)
    user_id = columns.UUID(primary_key=True,default=uuid.uuid4)
    password = columns.Text()

class userProcessor(modelProcessor):
    def writeModel(self, usr, passwd):
            self.model.create(username=usr, password=passwd)
    def readModel(self, usr):
         return self.model.get(username=usr)

