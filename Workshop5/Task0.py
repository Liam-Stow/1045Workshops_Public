#print elements of a list with indexes
def printElements(List):
    length = len(List)
    for i in  range(length):
        print("At index {} is the element {}".format(i, List[i]))


#Sort a list from smallest to largest
def selectionSort(List):
    length = len(List)
    for i in range(length):
        small = i
        #Find smallest in remaining list
        for j in range(i+1, length):
            if List[j] < List[small]:
                small = j
        #Swap index i with smallest
        temp = List[i]
        List[i] = List[small]
        List[small] = temp
        
    return List


def printAscending(List):
    _list = List[:]
    selectionSort(_list)
    printElements(_list)


printAscending([1,7,25,5837,916,42])
