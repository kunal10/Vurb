from grpc.beta import implementations

import data_pb2
import service_pb2


def run():
    channel = implementations.insecure_channel('localhost', 50051)
    stub = service_pb2.beta_create_DataRetrieval_stub(channel)

    response = stub.GetDeck("1")
    print response.deck.SerializeToString

    response = stub.GetUserDeck("1")
    print response.deck.SerializeToString


if __name__ == '__main__':
    run()
