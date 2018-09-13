'''
Test gRPC Client
'''

import grpc

import test_grpc_pb2
import test_grpc_pb2_grpc

def runClient():
    with grpc.insecure_channel('localhost:20800') as channel:
        stub = test_grpc_pb2_grpc.TestGrpcStub(channel)
        req = test_grpc_pb2.TestRequest()
        req.data = 'xliang'
        rsp = stub.TestHello(req)
        print('recv rsp code:%d msg:%s' % (rsp.code, rsp.msg))
        req = test_grpc_pb2.AddRequest()
        req.x = 10
        req.y = 32
        rsp = stub.Add(req)
        print('recv add rsp, code:%d result:%d' % (rsp.code, rsp.result))
    

if __name__ == '__main__':
    runClient()