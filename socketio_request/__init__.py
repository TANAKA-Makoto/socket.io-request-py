# -*- coding: utf-8 -*-

__version__ = '0.0.1'

from socketIO_client_nexus import SocketIO, BaseNamespace


class SocketIORequest:
    """docstring for SocketIORequest"""
    def __init__(self, io, options={}):
        super(SocketIORequest, self).__init__()
        self.arg = arg
        self.io = io
        self.options = {
            'event': 'socket.io-request',
            'timeout': 90000
        }.update(options)

    def on_request_ack(*args):
        self.io.removeListenr()
        pass

    def request(self, method, data):
        self.io.emit(self.options.event, {'method': method, 'data': data}, on_request_ack)
        pass

    def response(self, method, *middleares):
        pass
