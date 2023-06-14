from flask_socketio import SocketIO
from . import flask


def run():
    app = flask.get_app()
    app.config['SECRET_KEY'] = 'secret!'
    sio = SocketIO(app)
    sio.init_app(app, cors_allowed_origins='*')

    @sio.event
    def connection(sid):
        print(f'${sid} connected')

    @sio.event
    def disconnect(sid):
        print(f'${sid} disconnected')

    @sio.on('my event')
    def handle_my_custom_event(json):
        print('received json: ' + str(json))

    sio.run(app, debug=True, port=8080)

