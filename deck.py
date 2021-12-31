import random

class Deck:
    NORMAL_DECK = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]*4
    def __init__(self, length):
        self.cards = Deck.NORMAL_DECK*length
    def shuffle(self):
        random.shuffle(self.cards)



deck = Deck(4)
deck.shuffle()
print(deck.cards)