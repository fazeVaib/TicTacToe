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
    arr = [moveCondition_a(0, 1, 2), 
    moveCondition_a(3, 4, 5),
    moveCondition_a(6, 7, 8),
    moveCondition_a(0, 3, 6),
    moveCondition_a(1, 4, 7),
    moveCondition_a(2, 5, 8),
    moveCondition_a(2, 4, 6),
    moveCondition_a(0, 4, 8),
    moveCondition_b(0, 1, 2),
    moveCondition_b(3, 4, 5),
    moveCondition_b(6, 7, 8),
    moveCondition_b(0, 3, 6),
    moveCondition_b(1, 4, 7),
    moveCondition_b(2, 5, 8),
    moveCondition_b(2, 4, 6),
    moveCondition_b(0, 4, 8)]

    if arr[0] != -1:
        return arr[0]
    elif arr[1] != -1:
        return arr[1]
    elif arr[2] != -1:
        return arr[2]
    elif arr[3] != -1:
        return arr[3]
    elif arr[4] != -1:
        return arr[4]
    elif arr[5] != -1:
        return arr[5]
    elif arr[6] != -1:
        return arr[6]
    elif arr[7] != -1:
        return arr[7]
    elif arr[8] != -1:
        return arr[8]
    elif arr[9] != -1:
        return arr[9]
    elif arr[10] != -1:
        return arr[10]
    elif arr[11] != -1:
        return arr[11]
    elif arr[12] != -1:
        return arr[12]
    elif arr[13] != -1:
        return arr[13]
    elif arr[14] != -1:
        return arr[14]
    elif arr[15] != -1:
        return arr[15]
    else:
        return random.randint(0, 8)


def moveCondition_a(i, j, k):
    if (boardValues[i] == boardValues[j] == compSym and boardValues[k] == ' '):
        return k
    elif (boardValues[i] == boardValues[k] == compSym and boardValues[j] == ' '):
        return j
    elif (boardValues[k] == boardValues[j] == compSym and boardValues[i] == ' '):
        return i
    else:
        return -1

def moveCondition_b(i, j, k):
    if (boardValues[i] == boardValues[j] == playerSym and boardValues[k] == ' '):
        return k
    elif (boardValues[i] == boardValues[k] == playerSym and boardValues[j] == ' '):
        return j
    elif (boardValues[k] == boardValues[j] == playerSym and boardValues[i] == ' '):
        return i
    else:
        return -1

    

def computerTurn():
    num = GuessCompMove()
    while boardValues[num] != ' ':
        num = GuessCompMove()
    boardValues[num] = compSym
    displayBoard()

    if ifWon():
        print("YOU LOSE :(")
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
        print("YOU WON!")
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

def isDraw():
    if ' ' not in boardValues:
        print("MATCH DRAWN!")
        exit()

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
        isDraw()

