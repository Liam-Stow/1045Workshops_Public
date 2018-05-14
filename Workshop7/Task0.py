matrix =    [[11,12,13],
            [21,22,23],
            [31,32,33]]

matrixLength = len(matrix)

#Calculate [0][0] * [1][1] * [2][2] - [0][2] * [1][1] * [2][0]
first = 1
second = 1
print('  ', end='')
for i in range(matrixLength):
    print(matrix[i][i], end='')
    if i<matrixLength-1:
        print(' * ', end = '')
    first *= matrix[i][i]
    
print(' - ', end = '')

for i in range(matrixLength):
    print(matrix[i][matrixLength-1-i], end='')
    if i<matrixLength-1:
        print(' * ', end = '')
    second *= matrix[i][matrixLength-1-i]
    
print()
print('= {} - {}'.format(first, second))
print('=', first - second)
