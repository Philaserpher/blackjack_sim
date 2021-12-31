from deck import Deck
from player import getplay

#Set up constants
ITERATIONS = 1000

deck = Deck(4)
deck.shuffle()


def play():
    player_cards, dealer_cards = [], []
    for i in range(2):
        player_cards.append(deck.get_card())
        dealer_cards.append(deck.get_card())
    print(player_cards)
    print(dealer_cards)


play()