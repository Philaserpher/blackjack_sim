from deck import Deck
from players import Dealer, Player
from strategy import getplay

#Set up constants
ITERATIONS = 10000



def main():
    mydeck = Deck(8)
    mydeck.shuffle()
    myplayer = Player()
    mydealer = Dealer()
    total = 0
    for i in range(ITERATIONS):
        total += new_play(myplayer, mydealer, mydeck)
        if len(mydeck.cards) < 20:
            mydeck.add_decks(8)
    print(total)


def new_play(player, dealer, deck):
    player.empty_hand()
    dealer.empty_hand()
    for i in range(2):
        player.draw(deck)
        dealer.draw(deck)
    
    player_plays(player, dealer, deck)
    if sum(player.cards) > 21:
        return(-1)
    dealer_plays(dealer, deck)
    if sum(dealer.cards) > 21:
        return(1)
    if sum(player.cards) > sum(dealer.cards):
        return(1)
    return(-1)


def player_plays(player, dealer, deck):
    while sum(player.cards) < 21:
        choice = getplay(player.cards, dealer.cards[0])
        if choice == 1:
            player.draw(deck)
        elif choice == 0:
            break


def dealer_plays(dealer, deck):
    while sum(dealer.cards) < 17:
        dealer.draw(deck)



if __name__ == "__main__":
    main()