import random

Ace = 11
Jack = 10
King = 10
Queen = 10
cards = [Ace, 2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King] 

dealerHand = []
dealerCount = 0
userHand = []
userCount = 0

def runGame(): #runs the game
  deal()
  print("Your hand: ", userHand, "Count:", getUserCount())
  print("Dealers hand: ", dealerHand, "Count:", getDealerCount())
  
def deal():
  if len(dealerHand) == 0:
    dealerHand.append(random.choice(cards))
    dealerHand.append(random.choice(cards))
    
  if len(userHand) == 0:
    userHand.append(random.choice(cards))
    userHand.append(random.choice(cards))
    
def getDealerCount():
  total = 0
  for x in dealerHand:
    total = total + x
  return total
  
def getUserCount():
  total = 0
  for x in userHand:
    total = total + x
  return total
"""
def userCommands: #takes in a command
  
  #hit command 
  
  #stand command 
  
  #double down command 
  
  #bust functionality
  
def hit:
  #hit command draws another card
  
def stand:
  #stand command ends the users hand
  
def doubleD:
   #double down command doubles the user bet, can only be used on the first card and attomatically hits and stands for the user
   
def bust:
  #bust occurs if either user or dealer hand goes over 21
  
  
def dealer: # takes in the dealers hand count
  
  #dealer hits if the hand count is 16 or less
  
  #dealer stands if the hand count is 17 or more
  
def hasAce:
  #if either the user or dealer has an ace:
  
  #ace = 1 if the count > 21
  
  #ace = 11 if the count <= 21
  
  
startGame = input("Would you like to start the game? Enter yes or no: ")

if startGame == 'yes':
  
  """
runGame()
  