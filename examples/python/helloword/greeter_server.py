# -*- coding:utf-8 -*-
# Copyright 2015 gRPC authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""The Python implementation of the GRPC helloworld.Greeter server."""
import os
import sys
from concurrent import futures
import logging

p1 = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
sys.path.append(p1)

import grpc
from examples.python.helloword import helloworld_pb2_grpc, helloworld_pb2


class Greeter(helloworld_pb2_grpc.GreeterServicer):

    def SayHello(self, request, context):
        # import time
        # time.sleep(30)
        return helloworld_pb2.HelloReply(message='Hello, %s!' % request.name)

    def SayHelloAgain(self, request, context):
        return helloworld_pb2.HelloReply(message='Hello, %s!' % request.name)

    def SayHelloStream(self, request, context):
        i = 0
        name = request.name
        while i < 3:
            yield helloworld_pb2.HelloReply(message='Hello, %s!' % name)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    helloworld_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    # server.add_insecure_port('[::]:50051')
    addr = '127.0.0.1:50051'
    server.add_insecure_port(addr)
    server.start()
    print(f"Listen on {addr}")
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
