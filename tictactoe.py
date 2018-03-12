import random

boardValues = ['O', 'O', 'O', ' ', ' ', ' ', ' ', ' ', ' ']
compSym = ' '
playerSym = ' '


def displayBoard():
    print(' ', boardValues[6], ' | ', boardValues[7], ' | ', boardValues[8])
    print('-----------------')
    print(' ', boardValues[3], ' | ', boardValues[4], ' | ', boardValues[5])
    print('-----------------')
    print(' ', boardValues[0], ' | ', boardValues[1], ' | ', boardValues[2])


def firstturn():
    if random.randint(0, 1):
        return 'Computer'
    else:
        return 'Player'


def ifWon():
    if boardValues[0] == boardValues[1] == boardValues[2] != ' ' or \
        boardValues[3] == boardValues[4] == boardValues[5] != ' ' or \
        boardValues[6] == boardValues[7] == boardValues[8] != ' ' or \
        boardValues[3] == boardValues[0] == boardValues[6] != ' ' or \
        boardValues[1] == boardValues[4] == boardValues[7] != ' ' or \
        boardValues[2] == boardValues[5] == boardValues[8] != ' ' or \
        boardValues[0] == boardValues[4] == boardValues[8] != ' ' or \
        boardValues[2] == boardValues[4] == boardValues[6] != ' ':
        return True
    else:
        return False


def computerTurn():
    if ifWon():
        print("You Lose")
        quit()
    # TODO:


def playerTurn():
    input("Enter position to put %s", playerSym)
    if ifWon():
        print("You win")
        exit()
    print("")
    # TODO:


def makeYourTurn(turn):
    if turn == 'Computer':
        computerTurn()
    else:
        playerTurn()


def decideSymbol(firstWho):
    if firstWho == 'Computer':
        compSym = 'O'
        playerSym = 'X'
    else:
        compSym = 'X'
        playerSym = 'O'


if __name__ == '__main__':
    displayBoard()
    currentTurn = firstturn()
    decideSymbol(currentTurn)
    print("First turn is  of " + currentTurn)
    while(True):
        makeYourTurn(currentTurn)
