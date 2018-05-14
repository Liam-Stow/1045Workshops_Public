def printStars(k):
    print('*'*k)

def getFactorials(n):
    if n == 1:
        printStars(1)
        return [1]
    else:
        lstFactorials = getFactorials(n-1)
        currentFactorial = lstFactorials[-1] * n
        printStars(currentFactorial)
        lstFactorials.append(currentFactorial)
        return lstFactorials
     
 
n = int(input('n='))
if n < 0:
    print('Please use a positive n value')
else:
    print(getFactorials(n))
    
    
