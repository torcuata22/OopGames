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
    gameDeckList = shuffle(startingDeckList)
    currentCardDict = getCard(gameDeckList)
    currentCardRank = currentCardDict['rank']
    currentCardValue = currentCardDict['value']
    currentCardSuit = currentCardDict['suit']
    print('Starting card is: '+ currentCardRank + 'of' + currentCardSuit)
    print()
    
    #deal 8 cards, predict if next card will be higher or lower than previous
    for cardNumber in range(0, NCARDS):
        answer = input('Will the next card be higher or lower than the ' + currentCardRank + 'of' + currentCardSuit + '? Enter h or l')
        answer = answer.casefold() #forces it to be all lowercase
        nextCardDict = getCard(gameDeckList)
        nextCardRank = nextCardDict['rank']
        nextCardValue = nextCardDict['value']
        nextCardSuit = nextCardDict['suit']
        print('The next card is: '+ nextCardRank + 'of' + nextCardSuit)
        
    if answer == 'h':
        if nextCardValue > currentCardValue:
            print('You got it right! It was higher.You earned 20 points!')
            score +=20
        else:
            print('Sorry, you guessed wrong. You lose 15 points')
            score -=15
            
    elif answer == 'l':
        if nextCardValue < currentCardValue:
            print('You got it right! It was lower. You earned 20 points!')
            score +=20
        else:
            print('Sorry, you guessed wrong. You lose 15 points')
            score -=15 
            
    print('Your score is: ' + score)
    print()
    currentCardRank = nextCardRank
    currentCardValue = nextCardValue
    
    goAgain = input('Press Enter to play again, or q to quit: ')
    if goAgain == 'q':
        break
    print('OK, bye!')
        
    