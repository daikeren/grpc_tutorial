import grpc

import hello_pb2
import hello_pb2_grpc

channel = grpc.insecure_channel('localhost:50051')
stub = hello_pb2_grpc.HelloStub(channel)

name = hello_pb2.Name(value="World")
response = stub.Hello(name)

print(response.value)
