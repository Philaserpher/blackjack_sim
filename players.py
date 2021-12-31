#Main algorithm, determine how the player plays, will be based off basic strategy https://www.blackjackapprenticeship.com/blackjack-strategy-charts/

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

