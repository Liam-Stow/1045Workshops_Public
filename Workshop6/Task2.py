store=[]
knapsack=[]
knapsackWeightUsed=0
itemID = 0
totalValue = 0

#Ask for user input
File=open(input("Please enter file name with item details:"))
Weight = input("Please enter the capacity of the knapsack:")
Weight = int(Weight.strip(" Kg"))

#Create a table based on input file
for line in File:
    itemID += 1
    line = line.strip("\n")
    line = line.split("kg $")
    line[0] = int(line[0])
    line[1] = int(line[1])
    line.append(itemID)
    store.append(line)
File.close()

#Find the item with the smallest weight
def getMinWeight(store):
    Min = 0
    for item in range (len(store)):
        if store[item][0] < store[Min][0]:
            Min = item
    return store[Min]

#Move an item from the table into your knapsack
def steal(store, knapsackWeightUsed):
    itemToSteal = getMinWeight(store)
    knapsack.append(itemToSteal)
    knapsackWeightUsed += itemToSteal[0]
    store.remove(itemToSteal)
    return knapsackWeightUsed

#Constantly steal things until the knapsack is not full
while knapsackWeightUsed < Weight:
    knapsackWeightUnused = Weight - knapsackWeightUsed
    if getMinWeight(store)[0] < knapsackWeightUnused:
        knapsackWeightUsed = steal(store, knapsackWeightUsed)
    else:
        break
    
#Calc total value
for item in knapsack:
    totalValue += item[1]

#print the optimal solution
itemInKnapsackID = 0
print('Optimal answer: ', end = '')
for item in knapsack:
    itemInKnapsackID += 1
    print('item {}'.format(item[2]), end = '')
    if itemInKnapsackID < len(knapsack):
        print(' and ', end = '')
print(', value = ${}'.format(totalValue))
