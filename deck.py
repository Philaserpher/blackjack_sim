import random



class Deck:

    NORMAL_DECK = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]*4        # normal card deck, no jacks

    def __init__(self, n):
        self.cards = Deck.NORMAL_DECK*n                                 # put n decks in the shoe
    
    def shuffle(self):
        random.shuffle(self.cards)

    def get_card(self):
        return(self.cards.pop(0))                                       # return top card, remove from deck (essentially dealing card)

    def show(self):
        print(self.cards)

    def add_decks(self, n):
        self.cards += Deck.NORMAL_DECK*n                                # refill the shoe with n decks
        self.shuffle()



