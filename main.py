from deck import Deck
from players import Dealer, Player
from strategy import getplay


ITERATIONS = 100000                                         # set up number of iterations
MINIMUM_CARDS = 20                                          # set up minimum number of cards in the shoe


def main(iterations, minimum_cards):
    mydeck = Deck(8)
    mydeck.shuffle()                                        # generate deck object, shoe with 8 decks
    myplayer = Player()
    mydealer = Dealer()                                     # make player and dealer object
    total = 0                                               # total keeps track of score (+1 for player win, -1 for dealer win)
    for i in range(iterations):
        total += new_play(myplayer, mydealer, mydeck)
        if len(mydeck.cards) < minimum_cards:               # checks that the shoe never runs out of cards
            mydeck.add_decks(8)
    print(total)


def new_play(player, dealer, deck):
    player.empty_hand()
    dealer.empty_hand()
    for i in range(2):                                      # draws cards in the correct order (P, D, P, D)
        player.draw(deck)
        dealer.draw(deck)
    
    player_plays(player, dealer, deck)
    dealer_plays(dealer, deck)
    if sum(player.cards) > 21:                              # check winner 
        return(-1)
    if sum(dealer.cards) > 21:
        return(1)
    if sum(player.cards) > sum(dealer.cards):
        return(1)
    return(-1)


def player_plays(player, dealer, deck):
    while True:
        if sum(player.cards) > 21:
            if player.cards == checkAce(player.cards):
                break
            player.cards = checkAce(player.cards)

        choice = getplay(player.cards, dealer.cards[0])
        if choice == 1:
            player.draw(deck)
        elif choice == 0:
            break
        
        

def checkAce(cards):
    for index, card in enumerate(cards):
        if  card == 11:
            cards[index] = 1
    return(cards)


def dealer_plays(dealer, deck):
    while True:
        if sum(dealer.cards) > 18:
    
            if dealer.cards == checkAce(dealer.cards):
                break
            dealer.cards = checkAce(dealer.cards)
        dealer.draw(deck)
        dealer.cards = checkAce(dealer.cards)



if __name__ == "__main__":
    main(ITERATIONS, MINIMUM_CARDS)