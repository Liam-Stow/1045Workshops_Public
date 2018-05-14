#Sort the coins from highest to lowest
def sort():
    for k in range(len(denomination)):
        Max = k
        for l in range (k+1,len(denomination)):
            if denomination[Max] < denomination[l]:
               Max = l
        temp = denomination[k]
        denomination[k] = denomination[Max]
        denomination[Max] = temp
    return denomination

#Keep getting coins until target is reached
def getcoins():
    Used=[]
    Total=0
    while Total < Change:
        for i in denomination:
            if i <= Change - Total:
                Total+=i
                Used.append(i)
                break
    return Used

#Convert coin amounts to integer
def convertToInt(denomination):
    for Coin in range(len(denomination)):
        denomination[Coin]=int(denomination[Coin])
    return denomination

#Take user input
denomination=input("Please enter denominations:")
Change=int(input("Please enter the amount you want:"))

#Prepair inputs for use
denomination = denomination.split(",")
denomination = convertToInt(denomination)

#Take coins
sort()
Used=getcoins()

#Print the result
print("Your denominations: ", end="")
counted = []
for i in range(len(Used)):
    if Used[i] not in counted:
        count=1
        for coins in range(i+1,len(Used)):
            if Used[i]==Used[coins]:
                count+=1
                counted.append(Used[i])
        print(count,"x",Used[i],end="  ")