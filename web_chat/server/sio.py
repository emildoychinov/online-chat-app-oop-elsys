from flask_socketio import SocketIO

from .abstract import *
from .flask import FlaskServer 

class SocketServer(AbsServer, metaclass=Singleton):
    #__metaclass__ = Singleton
    sio = SocketIO()
    flsk = FlaskServer()

    def __handle__(self, event: str, handle: Callable):
        self.sio.on_event(event, handle)

    def __init__(self):
        def conn(sid):
            print(f'${sid} connected')

        def disconn(sid):
            print(f'${sid} disconnected')

        def custom(json):
            print('received json: ' + str(json))

        self.__handle__('connect', conn)
        self.__handle__('disconnect', disconn)
        self.__handle__('my event', custom)

        self.sio.init_app(self.flsk.app, cors_allowed_origins='*') 

    def run(self):
        self.sio.run(self.flsk.app, debug=self.debug, port=self.port)
