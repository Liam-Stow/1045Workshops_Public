numberOfCupcakesEaten = 0
totalMilesToRun = 0

#Get user input
noOfCupcakes = int(input('Please enter the number of cupcakes: '))
strCalorieCounts = input('Respective calorie counts of each cupcake: ')

#Store the calorie counts in a list
lstCalorieCounts = strCalorieCounts.split(' ')
for index, calorie in enumerate(lstCalorieCounts):
    lstCalorieCounts[index] = int(calorie)

#Calculate miles to run
def calcMilesToRun(cupcakeCalories):
    return totalMilesToRun + cupcakeCalories * 2**numberOfCupcakesEaten

#Eat a cupcake, add miles and remove from list
def eatCupcake(calories, totalMilesToRun):
    totalMilesToRun += calcMilesToRun(calories)
    lstCalorieCounts.remove(calories)
    return totalMilesToRun

#Figure out which cupcake to eat
#Returns index of the cupcake that will provide the least distance to run
def findBestCupcake():
    leastMilesToRun = calcMilesToRun(lstCalorieCounts[0])
    bestCupcakeIndex = 0
    for CupcakeIndex, calories in enumerate(lstCalorieCounts):
        milesToRun = calcMilesToRun(calories)
        if milesToRun < leastMilesToRun:
            leastMilesToRun = milesToRun
            bestCupcakeIndex = CupcakeIndex
    return bestCupcakeIndex
    
#Eat all the cupcakes!
while len(lstCalorieCounts) > 0:
    bestCupcake = findBestCupcake()
    totalMilesToRun = eatCupcake(lstCalorieCounts[bestCupcake], totalMilesToRun)
     
#Print the result
print('Marc should walk at least', totalMilesToRun, 'miles.')