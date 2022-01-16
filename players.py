# simple class for player and dealer, will have a hand, can draw cards and empty hand
# for now could be a single class, however will add splitting and doubling down later. Could use inheritance

class Dealer:
    def __init__(self):
        self.cards = []

    def draw(self, deck):
        self.cards.append(deck.get_card())

    def empty_hand(self):
        self.cards = []


class Player:
    def __init__(self):
        self.cards = []

    def draw(self, deck):
        self.cards.append(deck.get_card())

    def empty_hand(self):
        self.cards = []
