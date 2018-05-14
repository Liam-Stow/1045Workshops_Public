
#----TASK 1----

#Read in from file into aList
fileToLoad = input("Enter name of file: ")
fileToOpen = open(fileToLoad)
aList = []
for i in fileToOpen:
    i = i.strip() #Remove newline character
    aList.append(i.split(","))

#Print neatly
def printList(listToPrint):
    for x in listToPrint:
        print("{} kms, ${}".format(x[0], x[1]))

printList(aList)
