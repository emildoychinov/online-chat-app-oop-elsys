import uuid
import json
from cassandra.cqlengine import columns
from cassandra.cqlengine import connection
from datetime import datetime
from cassandra.cqlengine.models import Model
from .modelProcessor import modelProcessor


class message(Model):
    owner_id = columns.UUID()
    username = columns.Text()
    room_id = columns.UUID(primary_key=True)
    time_sent = columns.DateTime(primary_key=True, default=datetime.now(), clustering_order="ASC")
    content = columns.Text()

class messageProcessor(modelProcessor):
    @staticmethod
    def writeModel(self, ownerid, username, roomid, message_cnt):
            self.model.create(owner_id = ownerid, username = username, room_id = roomid, time_sent = datetime.now(), content=message_cnt)

    @staticmethod
    def readModel(self, roomid):
        try :
            msgs = self.model.objects(room_id = roomid)
        except : 
             return None
        messages = [json.dumps({'user' : msg.username, 'user_id' : str(msg.owner_id),  'content' : msg.content}) for msg in msgs]
        return messages
    
