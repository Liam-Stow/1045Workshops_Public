
#----TASK 1----

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
        print("{} kms, ${}".format(x[0], x[1]))


#----TASK 3----

def selectionSortPrice(listToSort):
    listLength = len(listToSort)
    for x in range (listLength):
        smallest = x
        #Find next smallest
        for y in range (x, listLength):
            if listToSort[y][1] < listToSort[smallest][1]:
                smallest = y
        #Swap smallest with current x
        temp = listToSort[smallest]
        listToSort[smallest] = listToSort[x]
        listToSort[x] = temp

    return listToSort


selectionSortPrice(aList)
printList(aList)
