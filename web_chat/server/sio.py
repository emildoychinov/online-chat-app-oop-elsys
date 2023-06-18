from flask_socketio import SocketIO
from .db import chat_Processor, message_Processor, user_Processor
from .abstract import *
from .flask import FlaskServer 
from flask import request


class SocketServer(AbsServer, metaclass=Singleton):
    sio = SocketIO()
    flsk = FlaskServer()
    sid = ''
    def __handle__(self, event: str, handle: Callable):
        self.sio.on_event(event, handle)

    def __init__(self):
        def conn():
            self.sio.server.enter_room(sid=request.sid, room="")
            print(f'${request.sid} connected')

        def custom(json):
            print('received json: ' + str(json))
        
        def change_room(room):
            self.sio.server.enter_room(sid=request.sid, room=str(room))
            print(f'${request.sid} joined room ${room}')

        def login(username, password):
                usr = user_Processor.readModel(username)
                if usr :
                    if(usr.password == password):
                        self.sio.emit("login_res", {'result' : 'true', 'id':str(usr.user_id)}, room="")
                    else :
                        self.sio.emit("login_res", {'result' : 'false'}, room="")
                else :
                    self.sio.emit("login_res", {'result' : 'false'}, room="")
                    
        def register(username, password, confirmed_password):
            usr = user_Processor.readModel(username)
            if password != confirmed_password :
                self.sio.emit("register_res", {'result' : 'false'}, room="")
            elif usr :
                self.sio.emit("register_res", {'result' : 'false'}, room="")
            else :
                user_Processor.writeModel(username, password)
                self.sio.emit("register_res", {'result' : 'true'}, room="")

        def get_rooms(usr):
            rooms = chat_Processor.readUserRooms(usr)
            print(rooms)
            self.sio.emit('user_rooms', rooms, room=str(usr))

        def get_messages(room_id):
            messages = message_Processor.readModel(room_id)
            self.sio.emit('messages', messages, room=str(room_id))

        def send_message(owner_id, room_id, content):
            username = user_Processor.readById(owner_id).username
            print("username : " + username)
            message_Processor.writeModel(owner_id, username, room_id, content)
            self.sio.emit('display_message',{'username' : username, 'user_id' : owner_id, 'content' : content}, room=str(room_id))

        def make_room(owner_id, room_name, member_list):
            member_set = set()
            for member in member_list :
                member_set.add(user_Processor.readModel(member).user_id)
            chat_Processor.writeModel(owner_id, room_name, member_set)
            
        self.__handle__('connect', conn)
        self.__handle__('my event', custom)
        self.__handle__('register', register)
        self.__handle__('login', login)
        self.__handle__('change_room', change_room)
        self.__handle__('get_rooms', get_rooms)
        self.__handle__('get_messages', get_messages)
        self.__handle__('send_message', send_message)
        self.__handle__('make_room', make_room)
        self.sio.init_app(self.flsk.app, cors_allowed_origins='*') 

    def run(self):
        self.sio.run(self.flsk.app, debug=self.debug, port=self.port)
