#Print the first n numbers
def printToN(n,current):
    current+=1    
    if current <= n:
        print(current)
        printToN(n,current)
        

#Print the first n square numbers
def printSquares(n,current):
    current+=1
    if current <= n:
        print(current*current)
        printSquares(n,current)

        
#Returns the sum of the first n square numbers
def sumOfSquares(n,total):
    if n != 0:
        total += n*n
        return sumOfSquares(n-1, total)
    else:
        return total

n=int(input("print the numbers 1 to n, where n="))
printToN(n,0)

n=int(input("Print the first n square numbers, where n="))
printSquares(n,0)

n=int(input("Return the sum of the first n square numbers, where n="))      
total = sumOfSquares(n,0)
print(total)
