import uuid
from cassandra.cqlengine import columns
from cassandra.cqlengine import connection
from datetime import datetime
from cassandra.cqlengine.models import Model
from .modelProcessor import modelProcessor


class message(Model):
    owner_id = columns.UUID()
    room_id = columns.UUID(primary_key=True)
    time_sent = columns.DateTime(primary_key=True, default=datetime.now(), clustering_order="DESC")
    content = columns.Text()

class messageProcessor(modelProcessor):
    def writeModel(self, ownerid, roomid, message_cnt):
            self.model.create(owner_id = ownerid, room_id = roomid, content=message_cnt)
    def readModel(self, roomid):
         return self.model.get(room_id = roomid)
