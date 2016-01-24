import data_pb2
import service_pb2
import time


def get_compressed_deck(deck):
    compressed_deck = data_pb2.Deck()
    compressed_deck.deckId = deck.deckId
    compressed_deck.description = deck.description
    return compressed_deck


class DataRetrievalServicer(service_pb2.BetaDataRetrievalServicer):
    """Implements functionality of DataRetrieval server"""

    def __init__(self):
        self.db = self.read_data()

    # TODO : Read data from input file.
    def read_data(self):
        decks = []
        deck = data_pb2.Deck()
        deck.userId = "1"
        deck.deckId = "1"
        deck.description = "deck 1 of user 1"
        deck.pageToken = 1
        deck.nextPageToken = 2

        card = data_pb2.Card()
        card.id = "1"
        card.title = "Restaurant 1"
        deck.cards["1"] = card

        decks.append(deck)
        return decks

    def GetDeck(self, request, context):
        deck_response = service_pb2.DeckResponse()
        for deck in self.db:
            if deck.deckId == request.deckId:
                deck_response.deck = deck
        return deck_response

    def GetUserDeck(self, request, context):
        user_deck_response = service_pb2.UserDeckResponse()
        for deck in self.db:
            if deck.userId == request.userId:
                if not request.paginated or request.pageToken == deck.pageToken:
                    user_deck_response.decks[deck.deckId] = get_compressed_deck(deck)
        return user_deck_response

    # TODO : Handle timeouts.
    def GetDetailedUserDeck(self, request, context):
        user_deck_response = self.GetUserDeck(request)
        detailed_user_deck_response = service_pb2.UserDeckResponse()
        for deckId in user_deck_response.decks:
            deck_request = service_pb2.DeckRequest()
            deck_request.deckId = deckId
            detailed_user_deck_response.decks[deckId] = self.GetDeck(deck_request).deck
        return detailed_user_deck_response


def serve():
    server = service_pb2.beta_create_DataRetrieval_server(DataRetrievalServicer())
    server.add_insecure_port('[::]:50051')
    server.start()
    try:
        while True:
            time.sleep(300)
    except KeyboardInterrupt:
        server.stop()


if __name__ == '__main__':
    serve()
