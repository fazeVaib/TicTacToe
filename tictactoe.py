import random

boardValues = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
compSym = 'X'
playerSym = 'O'


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


def GuessCompMove():
    return random.randint(0, 8)

def computerTurn():
    num = GuessCompMove()
    while boardValues[num] != ' ':
        num = GuessCompMove()
    boardValues[num] = compSym
    displayBoard()

    if ifWon():
        print("You Lose")
        quit()
        


def playerTurn():
    num = int(input('Your move on [1-9]: ').strip())
    while boardValues[num-1] != ' ':
        print('Already filled. Enter again!')
        num = int(input('Your move on: ').strip())
    boardValues[num-1] = playerSym
    print()
    displayBoard()

    if ifWon():
        print("You win")
        exit()

        
def makeYourTurn(turn):
    if turn == 'Computer':
        computerTurn()
    else:
        playerTurn()


def nextTurn(turn):
    if turn == 'Computer':
        return 'Player'
    else:
        return 'Computer'

# def decideSymbol(firstWho):
#     if firstWho == 'Computer':
#         compSym = 'O'
#         playerSym = 'X'
#     else:
#         compSym = 'X'
#         playerSym = 'O'


if __name__ == '__main__':
    displayBoard()
    currentTurn = firstturn()
    # decideSymbol(currentTurn)
    print("First turn is  of " + currentTurn)
    while(True):
        print('\n {} turn.\n'.format(currentTurn))
        makeYourTurn(currentTurn)
        currentTurn = nextTurn(currentTurn)

