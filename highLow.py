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

startingDeckList = []
#Each card is a dictionary (rank, suit, value). Retrieve first value of each tuple and save it in dict to make up card
for suit in SUIT_TUPLE:
    for thisValue, rank in enumerate(RANK_TUPLE):
        cardDict = {'rank': rank, 'suit': suit, 'value': thisValue+1}
        startingDeckList.append(cardDict)
score = 50

#to play multiple rounds:
while True:
    print()
    