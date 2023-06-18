from models.modelProcessor import modelProcessor
from models.chat_model import chat_room,chatProcessor
from models.message_model import message,messageProcessor
from models.user_model import user,userProcessor
from cassandra.cqlengine import connection

connection.setup(['localhost'], "web_chat", protocol_version=3)

chat_Processor = chatProcessor(chat_room)
message_Processor = messageProcessor(message)
user_Processor = userProcessor(user)

chat_Processor.constructTable()
message_Processor.constructTable()
user_Processor.constructTable()