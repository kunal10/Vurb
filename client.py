from grpc.beta import implementations

import data_pb2
import service_pb2


def run():
    channel = implementations.insecure_channel('localhost', 50051)
    stub = service_pb2.beta_create_DataRetrieval_stub(channel)

    request = service_pb2.DeckRequest()
    request.deckId = "1"
    response = stub.GetDeck(request)
    print response.deck.SerializeToString

    request = service_pb2.UserDeckRequest()
    request.userId = "1"
    request.pageToken = 1
    response = stub.GetUserDeck(request)
    print response.deck.SerializeToString

    response = stub.GetDetailedUserDeck(request)
    print response.deck.SerializeToString


if __name__ == '__main__':
    run()
