from flask import Flask,redirect, url_for
from flask_socketio import SocketIO, emit
from websocket.sock_namespace import *
from websocket.live import *

# configuration

def create_app(debug=False):
    app = Flask(__name__)
    app.config.from_object(__name__)
    app.config.from_envvar('FLASKR_SETTINGS', silent=True)
    app.register_blueprint(live)
    app.debug=debug

    app.config['TEMPLATES_AUTO_RELOAD']=True
    app.jinja_env.auto_reload = True

    @app.route('/')
    def index():
        return redirect(url_for('live.dash_live'))

    return app
