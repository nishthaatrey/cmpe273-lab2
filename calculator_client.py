from __future__ import print_function

import grpc

import calculator_pb2
import calculator_pb2_grpc


def run():
    channel = grpc.insecure_channel('localhost:50051')
    stub = calculator_pb2_grpc.CalculatorStub(channel)
   
    response = stub.add(calculator_pb2.CalculatorRequest(a=1,b=2))
    print("Sum is: " + response.message)

if __name__ == '__main__':
    run()