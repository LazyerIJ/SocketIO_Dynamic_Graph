from socketIO_client import SocketIO, BaseNamespace
import random
import time

host = "127.0.0.1"
port = 8010
namespace = '/livedata'

class ChatNamespace(BaseNamespace):
    def on_test_response(self, *args):
        pass


if __name__=='__main__':

    test_cnt = 10000
    socketIO = SocketIO(host, port)
    chat_namespace = socketIO.define(ChatNamespace, namespace)
    freq = 120
    ymax = 1000
    ymin = -1000
    length = 5

    for i in range(test_cnt):
        data = [random.randint(ymin, ymax) for x in range(length)]
        chat_namespace.emit('dash_event', {'data':data})
        time.sleep(1/(freq/length))
