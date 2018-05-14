#Checks if a queen position is valid given a
#particular arrangement of existing queens
#on a chess board.
def checkQueen(y, x, chessBoard):
    LENGTH = len(chessBoard) - 1

    #Check upper boundaries
    if (x > LENGTH) or (y > LENGTH):
        return False

    #Check lower boundaries
    if (x < 0) or (y < 0):
        return False

    #Check for a existing queen on that spot
    if chessBoard[y][x] == 1:
        return False
    
    return True

#Create empty chess board
N = int(input("Enter N: "))
chessBoard = []
for i in range(N):
    chessBoard.append([0]*N)

#Ask the user for queen positions
noOfQueens = 0
while noOfQueens < N:
    newQueen = input("Enter position of Queen: ")
    newQueen = newQueen.split(' ')
    newQueen[0] = int(newQueen[0])
    newQueen[1] = int(newQueen[1])
    if checkQueen(newQueen[0], newQueen[1], chessBoard):
        #Save that position as a queen
        chessBoard[newQueen[0]][newQueen[1]] = 1
        noOfQueens += 1
    else:
        print('Invalid Queen! Try again.')

print(chessBoard)
