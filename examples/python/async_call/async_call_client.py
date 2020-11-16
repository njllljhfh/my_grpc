# -*- coding:utf-8 -*-
# 测试异步client调用
import time

import grpc

from examples.python.async_call import async_call_pb2_grpc as pb2_grpc
from examples.python.async_call import async_call_pb2 as pb2

class RpcHandler:
    def rpc_async_req(self, stub):
        def process_response(future):
            duck.quack(future.result().quackMsg)

        duck = Duck()
        call_future = stub.Quack.future(pb2.QuackRequest(quackTimes=5)) #non-blocking call
        call_future.add_done_callback(process_response) #non-blocking call
        print('sent request, we could do other stuff or wait, lets wait this time. . .')
        time.sleep(12) #the main thread would drop out here with no results if I don't sleep
        print('exiting')

class Duck:
    def quack(self, msg):
        print(msg)


def main():
    channel = grpc.insecure_channel('localhost:12345')
    stub = pb2_grpc.DuckServiceStub(channel)
    rpc_handler = RpcHandler()
    rpc_handler.rpc_async_req(stub=stub)

if __name__ == '__main__':
    main()