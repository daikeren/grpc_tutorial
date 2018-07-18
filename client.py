import grpc

import hello_pb2
import hello_pb2_grpc

channel = grpc.insecure_channel('localhost:50051')
stub = hello_pb2_grpc.HelloStub(channel)

request = hello_pb2.HelloRequest(value="World")
response = stub.Hello(request)

print(response.value)
