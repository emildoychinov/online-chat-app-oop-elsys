from server import * 
from server.models.chat_model import chat_room,chatProcessor
from server.models.message_model import message,messageProcessor
from server.models.user_model import user,userProcessor
from cassandra.cqlengine import connection

def run():
    connection.setup(['localhost'], "web_chat", protocol_version=3)
    print('database connection established')

    chat_Processor = chatProcessor(chat_room)
    message_Processor = messageProcessor(message)  
    user_Processor = userProcessor(user)

    chat_Processor.constructTable() 
    message_Processor.constructTable()
    user_Processor.constructTable()

    srv = SocketServer()
    srv.run()