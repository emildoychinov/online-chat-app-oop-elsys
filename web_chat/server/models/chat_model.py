import uuid
from cassandra.cqlengine import columns
from cassandra.cqlengine import connection
from datetime import datetime
from cassandra.cqlengine.models import Model
from .modelProcessor import modelProcessor

class chat_room(Model):
    owner_id = columns.UUID(primary_key=True)
    room_id = columns.UUID(default=uuid.uuid4)
    name = columns.Text(required=False)
    users = columns.Set(columns.UUID, default = uuid.uuid4)

class chatProcessor(modelProcessor):
    def writeModel(self, ownerid, chat_name, chat_users):
            self.model.create(owner_id = ownerid, name = chat_name, users=list(chat_users))
    def readModel(self, ownerid):
         return self.model.get(owner_id = ownerid)
         #return super().readModel(*args)