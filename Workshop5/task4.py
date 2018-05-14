#Read in from file into aList
fileName = input("Enter name of file: ")
file = open(fileName)
aList = []
for line in file:
    line = line.strip()
    line = line.split(',')
    line[0] = int(line[0])
    line[1] = float(line[1])
    aList.append(line)
file.close()
    
#Print neatly
def printList(listToPrint):
    for x in listToPrint:
        print(str(x[0]) + " kms, $" + str(x[1]))


def sortByElement(aList, element):
    listLength = len(aList)
    for x in range (listLength):
        smallest = x
        for y in range (x, listLength):
            #Find Smallest
            if aList[y][element] < aList[smallest][element]:
                smallest = y
        #Swap smallest with current x
        temp = aList[smallest]
        aList[smallest] = aList[x]
        aList[x] = temp

    return aList


def selectionSortDistance(listToSortByDistance):
    sortByElement(listToSortByDistance, 0)
    return listToSortByDistance


def listToSortByPrice(listToSortByPrice):
    sortByElement(listToSortByPrice, 1)
    return listToSortByPrice


while True:
    userInput = input("Enter choice Print, Sort1(distance), Sort2(price) or Quit: ").lower()
    if userInput.lower() == "print":
        printList(aList)
        
    elif userInput.lower() == "sort1":
        selectionSortDistance(aList)

    elif userInput.lower() == "sort2":
        listToSortByPrice(aList)
        
    elif userInput.lower() == "quit":
        break
    
    else:
        print("Please enter a valid input. ")




