from .server import *
from .server.db import chat_Processor, message_Processor, user_Processor
from cassandra.cqlengine import connection

def run():
    connection.setup(['localhost'], "web_chat", protocol_version=3)
    print('database connection established')

    chat_Processor.constructTable() 
    message_Processor.constructTable()
    user_Processor.constructTable()

    srv = SocketServer()
    srv.run()