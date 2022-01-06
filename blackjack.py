import random

Ace = 11
Jack = 10
King = 10
Queen = 10
cards = [Ace, 2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King] 

endGame = False
dealerHand = []
userHand = []

def runGame(): #runs the game
  deal()
  
  print("Your hand: ", userHand, "Count:", getUserCount())
  print("Dealers hand: ", dealerHand, "Count:", getDealerCount())
 
  while bust(getUserCount) == False:
    if endGame == True:
      break
    print("Would you like to hit, stand or double?")
    userCommands(input())
  else:
    print("bust")
   
def deal():
  dealerHand.append(random.choice(cards))
  dealerHand.append(random.choice(cards)) 
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

def userCommands(cmd): #takes in a command
  if cmd == "hit": hit(userHand)     
  if cmd == "stand": stand()
  #if cmd == "double": doubleD()

def hit(hand): #takes either userHand or dealerHand as an argument and adds draws a card
  hand.append(random.choice(cards))
  return print("Your hand: ", userHand, "Count:", getUserCount(),"\n", "Dealers hand: ", dealerHand, "Count:", getDealerCount())
  
def stand(): #stand command ends the users hand
  dealer()
  return result() 
  return endGame == True
  
#def doubleD(): #double down command doubles the user bet, can only be used on the first card and attomatically hits and stands for the user
   
def dealer(): # takes getDealerCount as an argument
  while getDealerCount() <= 16:
    hit(dealerHand)
    
def bust(count): #checks for bust, takes in a function argument i.e getUserCount or getDealerCount
  if count() > 21:
    return True
  if count() <= 21:
    return False
  
def result():
################################
  #user wins
  dealerBustsUserDoesnt = bust(getDealerCount()) == True and bust(getUserCount()) == False
  userHasHighCountNoBust = bust(getUserCount()) == False and bust(getDealerCount()) == False and getUserCount() > getDealerCount()
  userWin = dealerBustsUserDoesnt and userHasHighCountNoBust
  if userWin == True:
    return print("User Win")
##################################
  #dealer wins
  elif getDealerCount() < getUserCount() and getUserCount() <= 21:
    return print("User Won")
##################################
  #ties
  else:
    return print("Tie")
  
  
  """
  

def hasAce:
  #if either the user or dealer has an ace:
  
  #ace = 1 if the count > 21
  
  #ace = 11 if the count <= 21
  
  
startGame = input("Would you like to start the game? Enter yes or no: ")

if startGame == 'yes':
  
  """
runGame()
  