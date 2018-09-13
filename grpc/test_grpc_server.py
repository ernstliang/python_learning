'''
Test gRPC server
'''

from concurrent import futures
import time

import grpc
import test_grpc_pb2
import test_grpc_pb2_grpc

_ONE_DAY_IN_SECONDS = 60 * 60 * 24

class MyTestgRPC(test_grpc_pb2_grpc.TestGrpcServicer):
    def TestHello(self, request, content):
        print('recv reqest:%s' % request.data)
        print('content: ', content)
        return test_grpc_pb2.TestResponse(code=0, msg='Hello, %s!' % request.data)

    def Add(self, request, content):
        print('Add %d + %d' % (request.x, request.y))
        return test_grpc_pb2.AddResponse(code=0, result=request.x + request.y)

def runServer():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=5))
    test_grpc_pb2_grpc.add_TestGrpcServicer_to_server(MyTestgRPC(), server)
    server.add_insecure_port('[::]:20800')
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)
    
if __name__ == '__main__':
    runServer()
