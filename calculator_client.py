from __future__ import print_function

import grpc

import calculator_pb2
import calculator_pb2_grpc


def run():
    channel = grpc.insecure_channel('127.0.0.1:50051')
    stub = calculator_pb2_grpc.CalculatorServiceStub(channel)
   
    addNum = calculator_pb2.CalculatorRequest(num1=1,num2=5)
    response = stub.Add(addNum)
    print("Sum is: " + str(response.sum))

if __name__ == '__main__':
    run()
