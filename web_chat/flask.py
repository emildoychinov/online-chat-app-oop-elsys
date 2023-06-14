from flask import Flask, render_template

def get_app():
    app = Flask(__name__,
            static_folder='../client/static',
            template_folder='../client/html')

    @app.route('/')
    def home():
        return render_template('index.html')

    return app

"""
def run():
    app = get_app()
    app.run(debug=True, port=1337)
"""
