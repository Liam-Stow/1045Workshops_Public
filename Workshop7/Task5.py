#Checks if a queen position is valid
def checkQueen(y, x, queenPositions):
    LENGTH = len(queenPositions) - 1

    #Check upper boundaries
    if (x > LENGTH) or (y > LENGTH):
        return False

    #Check lower boundaries
    if (x < 0) or (y < 0):
        return False

    #Check for a existing queen on that spot
    if queenPositions[x] == y:
        return False
    
    return True

#Print queenPositions as a matrix
def printListInTableFormat(queenPositions):
    for rowNum in range(len(queenPositions)):
        for queenRow in queenPositions:
            if queenRow == rowNum:
                print(1, end=' ')
            else:
                print(0, end=' ')
        print() #newline
        
def checkSolution(queenPositions):
    LENGTH = len(queenPositions)
    
    #Check the y axis by making sure there are enough queens.
    '''If the user entered multiple queens in the same column,
    the queenPositions representation wouldn't store the 
    positions correctly, and we would end up with less than N
    queen in our final candidate solution.'''
    for queen in queenPositions:
        if queen == None:
            return False
    
    #Check the x axis
    for queenIndex in range(LENGTH):
        for remainingQueenIndicies in range(queenIndex+1, LENGTH):
            if queenPositions[queenIndex] == queenPositions[remainingQueenIndicies]:
                return False
    
    #Check upward diagional
    for queenIndex in range(LENGTH):
        y = queenPositions[queenIndex]
        x = queenIndex
        while x > 0 and y > 0:
            x -= 1
            y -= 1
            if y == queenPositions[x]:
                return False
    
    #Check downward diagional
    for queenIndex in range(LENGTH):
        y = queenPositions[queenIndex]
        x = queenIndex
        while x > 0 and y < LENGTH-1:
            x -= 1
            y += 1
            if y == queenPositions[x]:
                return False
    
    return True
    
#Create empty list of possible queen positions
N = int(input("Enter N: "))
queenPositions = [None]*N

#Ask the user for queen positions
noOfQueens = 0
while noOfQueens < N:
    newQueen = input("Enter position of Queen: ")
    newQueen = newQueen.split(' ')
    newQueen[0] = int(newQueen[0])
    newQueen[1] = int(newQueen[1])
    if checkQueen(newQueen[0], newQueen[1], queenPositions):
        #Save that position as a queen
        queenPositions[newQueen[1]] = newQueen[0]
        noOfQueens += 1
    else:
        print('Invalid Queen! Try again.')

print(queenPositions)
printListInTableFormat(queenPositions)

if checkSolution(queenPositions):
    print('that works')
else:
    print('that failed')
