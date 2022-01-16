# for now simplest strategy, will never go bust. dealer_card is not used here,
# but will in the future when incorporating a strategy

def getplay(player_cards, dealer_card):
    if sum(player_cards) < 12:
        return(1)
    return(0)
