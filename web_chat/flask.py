from flask import Flask, render_template

def app():
    app = Flask(__name__,
            static_folder='../client/static',
            template_folder='../client/html')

    @app.route('/')
    def home():
        return render_template('index.html')

    return app

def run():
    app = app()
    app.run(debug=True, port=1337)
