import random

print("Welcome to ABA")

possibleNumbers = [1,2,3,4,5,6,7,8,9]
gameBoard = [[1,2,3], [4,5,6], [7,8,9]]
rows = 3
cols = 3

def printGameBoard():
  for x in range(rows):
    print("\n+---+---+---+")
    print("|", end="")
    for y in range(cols):
      print("", gameBoard[x][y], end=" |")
  print("\n+---+---+---+")

def modifyArray(num, turn):
  num -= 1
  if(num == 0):
    gameBoard[0][0] = turn
  elif(num == 1):
    gameBoard[0][1] = turn
  elif(num == 2):
    gameBoard[0][2] = turn
  elif(num == 3):
    gameBoard[1][0] = turn
  elif(num == 4):
    gameBoard[1][1] = turn
  elif(num == 5):
    gameBoard[1][2] = turn
  elif(num == 6):
    gameBoard[2][0] = turn
  elif(num == 7):
    gameBoard[2][1] = turn
  elif(num == 8):
    gameBoard[2][2] = turn

### Define function to check for a winner
def checkForWinner(gameBoard):
  
  ### X axis
  if(gameBoard[0][0] == 'A' and gameBoard[0][1] == 'A' and gameBoard[0][2] == 'A'):
    print("A has won!")
    return "A"
  elif(gameBoard[0][0] == 'B' and gameBoard[0][1] == 'B' and gameBoard[0][2] == 'B'):
    print("B has won!")
    return "B"
  elif(gameBoard[1][0] == 'A' and gameBoard[1][1] == 'A' and gameBoard[1][2] == 'A'):
    print("A has won!")
    return "A"
  elif(gameBoard[1][0] == 'B' and gameBoard[1][1] == 'B' and gameBoard[1][2] == 'B'):
    print("B has won!")
    return "B"
  elif(gameBoard[2][0] == 'A' and gameBoard[2][1] == 'A' and gameBoard[2][2] == 'A'):
    print("A has won!")
    return "A"
  elif(gameBoard[2][0] == 'B' and gameBoard[2][1] == 'B' and gameBoard[2][2] == 'B'):
    print("B has won!")
    return "B"

  ### Y axis
  if(gameBoard[0][0] == 'A' and gameBoard[1][0] == 'A' and gameBoard[2][0] == 'A'):
    print("A has won!")
    return "A"
  elif(gameBoard[0][0] == 'B' and gameBoard[1][0] == 'B' and gameBoard[2][0] == 'B'):
    print("B has won!")
    return "B"
  elif(gameBoard[0][1] == 'A' and gameBoard[1][1] == 'A' and gameBoard[2][1] == 'A'):
    print("A has won!")
    return "A"
  elif(gameBoard[0][1] == 'B' and gameBoard[1][1] == 'B' and gameBoard[2][1] == 'B'):
    print("B has won!")
    return "B"
  elif(gameBoard[0][2] == 'A' and gameBoard[1][2] == 'A' and gameBoard[2][2] == 'A'):
    print("A has won!")
    return "A"
  elif(gameBoard[0][2] == 'B' and gameBoard[1][2] == 'B' and gameBoard[2][2] == 'B'):
    print("B has won!")
    return "B"

  ### Cross wins
  elif(gameBoard[0][0] == 'A' and gameBoard[1][1] == 'A' and gameBoard[2][2] == 'A'):
    print("A has won!")
    return "A"
  elif(gameBoard[0][0] == 'B' and gameBoard[1][1] == 'B' and gameBoard[2][2] == 'B'):
    print("B has won!")  
    return "B"
  elif(gameBoard[0][2] == 'A' and gameBoard[1][1] == 'A' and gameBoard[2][0] == 'A'):
    print("A has won!")  
    return "A"
  elif(gameBoard[0][2] == 'B' and gameBoard[1][1] == 'B' and gameBoard[2][0] == 'B'):
    print("B has won!") 
    return "B" 
  else:
    return "N"
  
leaveLoop = False
turnCounter = 0

while(leaveLoop == False):
         
  ### It's the player turn
  if(turnCounter % 2 == 0):
    printGameBoard()
    numberPicked = int(input("\nChoose a number [1-9]: "))
    if(numberPicked >= 1 or numberPicked <= 9):
      modifyArray(numberPicked, 'X')
      possibleNumbers.remove(numberPicked)
    else:
      print("Invalid input. Please try again.")
    turnCounter += 1
         
  ### It's the computer's turn
  else:
    while(True):
      cpuChoice = random.choice(possibleNumbers)
      print("\nCpu choice: ", cpuChoice)
      if(cpuChoice in possibleNumbers):
        modifyArray(cpuChoice, 'O')
        possibleNumbers.remove(cpuChoice)
        turnCounter += 1
        break
  
  winner = checkForWinner(gameBoard)
  if(winner != "N"):
    print("\nGame over!")
    break
