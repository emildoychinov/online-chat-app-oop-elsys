import uuid
import json
import traceback
from cassandra.cqlengine import columns
from cassandra.cqlengine import connection
from datetime import datetime
from cassandra.cqlengine.models import Model
from .modelProcessor import modelProcessor

class chat_room(Model):
    owner_id = columns.UUID()
    room_id = columns.UUID(default=uuid.uuid4)
    name = columns.Text(primary_key=True)
    users = columns.Set(columns.UUID, default = uuid.uuid4, index=True)

class chatProcessor(modelProcessor):
    @staticmethod
    def writeModel(self, ownerid, chat_name, chat_users):
            self.model.create(owner_id = ownerid, name = chat_name, users=list(chat_users))

    @staticmethod
    def readModel(self, name):
        try :
              room = self.model.get(name = name)
        except :
             return None
        return room         
    
    @staticmethod
    def readUserRooms(self, uid):
        try :
            result = self.model.objects.all()
        except Exception as e:
             return None
        
        filter_results = [json.dumps({'name' : room.name, 'id' : str(room.room_id)}) for room in result if uid in [str(usr) for usr in room.users]]
             
        return filter_results
    #return super().readModel(*args)
