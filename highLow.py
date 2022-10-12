import random

#Build deck:
SUIT_TUPLE = ('Spades', 'Hearts', 'Clubs', 'Diamonds')
RANK_TUPLE = ('Ace', '1', '2', '3','4', '5', '6','7', '8', '9','10', 'Jack', 'Queen', 'King')
NCARDS = 8

#To return random card from deck:
def getCard(deckListIn):
    thisCard = deckListIn.pop()
    return thisCard

#to return shuffled copy of the deck:
def shuffle(deckListIn):
    deckListOut = deckListIn.copy()
    random.shuffle(deckListOut)
    return deckListOut

#Game:
print('Welcome to Higher or Lower')
print('/n')
print ('You have to guess if the next card will be higher or lower than the current card')
print('/n')
print('If you guess right, you get 20 points. If not, you loose 15 points')
print('/n')
print('You have 50 points to start. Go!')