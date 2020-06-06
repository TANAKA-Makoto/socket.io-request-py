# -*- coding: utf-8 -*-

__version__ = '0.0.1'

from socketIO_client_nexus import SocketIO, BaseNamespace
import inspect


class SocketIORequest:
    """docstring for SocketIORequest"""
    methods = []
    options = None
    io = None

    def __init__(self, io, options={}):
        self.io = io
        self.options = {
            'event': 'socket.io-request',
            'timeout': 90000
        }
        self.options.update(options)

    def on_request_ack(*args):
        self.io.removeListenr()
        pass


    def request(self, method, data):
        self.io.emit(self.options['event'], {'method': method, 'data': data}, on_request_ack)
        pass

    def response(self, method, callback):
        """
         *callback: function pointer
        """
        def response_callback(req, ack):
            if (method not in self.methods):
                return
            res = {'data': callback(req['data'])}
            ack(res)

        if not isinstance(method, str):
            return  # error ('argument "method" is missing')
        if not inspect.isfunction(callback):
            return  # error ('"callback" must be a function')
        self.methods.append(method)
        self.io.on(self.options['event'], response_callback)
