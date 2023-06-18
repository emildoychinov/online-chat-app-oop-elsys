from flask import Flask, render_template

from .abstract import *

class FlaskServer(AbsServer, metaclass=Singleton):
    app = Flask(__name__,
                static_folder='../../client/static',
                template_folder='../../client/html')
    app.config['SECRET_KEY'] = 'secret!' # this is for socket.io communication later

    def __handle__(self, endpoint: str, handle: Callable[[None], None]):
        # same as 
        # @self.app.route(endpoint)
        # def handle(...):
        #    ...
        self.app.add_url_rule(endpoint, view_func=handle)

    def __init__(self):
        def home():
            return render_template('index.html')

        self.__handle__('/', home)


    def run(self):
        self.app.run(debug=self.debug, port=self.port)

