#!/usr/bin/env python
from threading import Lock
from flask import Flask, render_template, session, request
from flask_socketio import SocketIO, Namespace, emit, join_room, leave_room, \
    close_room, rooms, disconnect
import socketio
thread = None
thread_lock = Lock()


class MyNamespace(Namespace):

    def on_my_event(self, message):
        emit('my_response',
             {'data': message['data']})

    def on_join(self, message):
        join_room(message['room'])

    def on_dash_event(self, message):
        emit('livedash',{'data': message['data'] },room="test")

    def on_disconnect_request(self):
        emit('my_response',
             {'data': 'Disconnected!'})
        disconnect()

    def on_disconnect(self):
        pass

