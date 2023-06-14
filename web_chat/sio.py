from flask_socketio import SocketIO
from . import flask


def run():
    app = flask.app()
    sio = SocketIO(app)
    sio.init_app(app, cors_allowed_origins=['*'])

    @sio.event
    def connection(sid):
        print(f'${sid} connected')

    @sio.event
    def disconnect(sid):
        print(f'${sid} disconnected')

    sio.run(app, debug=True, port=1337)

