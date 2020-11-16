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
"""The Python implementation of the GRPC helloworld.Greeter client."""

# from __future__ import print_function
import logging
import os
import sys
import time

# p1 = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
# sys.path.append(p1)

import grpc
from examples.python.helloword import helloworld_pb2_grpc, helloworld_pb2


def run():

    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = helloworld_pb2_grpc.GreeterStub(channel)
        # 同步调用
        response = stub.SayHello(helloworld_pb2.HelloRequest(name='you'))
        print("Greeter client received: " + response.message)

        response = stub.SayHelloAgain(helloworld_pb2.HelloRequest(name='good'))
        print("Greeter client received: " + response.message)

if __name__ == '__main__':
    logging.basicConfig()
    run()
# - - - - - - -

# class RpcHandler(object):
#     def rpc_async_req(self, stub):
#         # 异步调用
#         feature_future = stub.SayHello.future(helloworld_pb2.HelloRequest(name='you'))
#         feature_future.add_done_callback(callback)
#         for i in range(8):
#             print(i)
#             time.sleep(1)
#
#
# def callback(feature):
#     response = feature.result()
#     print("Greeter client received: " + response.message)
#
#
# if __name__ == '__main__':
#     channel = grpc.insecure_channel('localhost:50051')
#     stub = helloworld_pb2_grpc.GreeterStub(channel)
#
#     rpc_handler = RpcHandler()
#     rpc_handler.rpc_async_req(stub=stub)
# - - - -

# class RpcHandler:
#     def rpc_async_req(self, stub):
#         def process_response(future):
#             duck.quack(future.result().message)
#
#         duck = Duck()
#         call_future = stub.SayHello.future(helloworld_pb2.HelloRequest(name='you'))  # non-blocking call
#         call_future.add_done_callback(process_response)  # non-blocking call
#         print('sent request, we could do other stuff or wait, lets wait this time. . .')
#         for i in range(10):
#             print(i)
#             time.sleep(2)
#         print('exiting')
#
#
# class Duck:
#     def quack(self, msg):
#         print(msg)
#
#
# def main():
#     channel = grpc.insecure_channel('localhost:50051')
#     stub = helloworld_pb2_grpc.GreeterStub(channel)
#     rpc_handler = RpcHandler()
#     rpc_handler.rpc_async_req(stub=stub)
#
#
# if __name__ == '__main__':
#     main()
