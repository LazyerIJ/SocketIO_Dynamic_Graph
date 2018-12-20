from websocket import create_app
from websocket.sock_namespace import *
from flask_socketio import SocketIO, emit
host = "127.0.0.1"
port=8010

app = create_app(debug=True)
socketio = SocketIO(app=app, async_mode=None)
socket_namespace = MyNamespace('/livedata')
socketio.on_namespace(socket_namespace)

if __name__ == "__main__":
    socketio.run(app=app, host=host, port=port)
