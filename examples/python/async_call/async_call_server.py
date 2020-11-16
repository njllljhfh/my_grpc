# -*- coding:utf-8 -*-
import time
from concurrent import futures

import grpc

from examples.python.async_call import async_call_pb2_grpc as pb2_grpc
from examples.python.async_call import async_call_pb2 as pb2


class DuckServer(pb2_grpc.DuckServiceServicer):
    def Quack(self, request, context):
        print('quack called...takes many cpu cycles to calculate...')
        time.sleep(10)
        quack_msg = 'quack ' * request.quackTimes
        return pb2.QuackResponse(quackMsg=quack_msg)


if __name__ == '__main__':
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    duck_serv = DuckServer()
    pb2_grpc.add_DuckServiceServicer_to_server(duck_serv, server)
    server.add_insecure_port('localhost:12345')
    server.start()
    print('server started. . .')
    try:
        while True:
            time.sleep(64 * 64 * 100)
    except KeyboardInterrupt:
        print('stopping server. . .')
        server.stop(None)