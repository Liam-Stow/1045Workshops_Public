#Read in a file of locations into a list
def readIn(fileName):
    
    file = open(fileName)
    locations = []

    for line in file:
        line = line.strip()
        line = line.split('\t')
        postcode = int(line[0])
        line[1] = line[1].split(',')
        for place in line[1]:
            locations.append([postcode, place])

    file.close()

    return locations


#Print the table nicely
def printNicely(locaitons):
    for place in locations:
        print(place[0], place[1])


#Sort in alphabetical order
def sort(locations):
    for k in range(len(locations)):
        MinValue = locations[k][1]
        Min = k
        for l in range (k+1,len(locations)):
            if MinValue > locations[l][1]:
                MinValue = locations[l][1]
                Min = l
                temp = locations[k]
        locations[k] = locations[Min]
        locations[Min] = temp
    return locations


#Recursivley search the list for a location name, return its index
def binarySearch2(locations,name,minIndex,maxIndex):
    midIndex = (minIndex + maxIndex) // 2
    mid = locations[midIndex]
    if (maxIndex-minIndex == 1) and (mid[1] != name):
        return None
    if mid[1] == name:
        return midIndex
    elif name < mid[1]:
        return binarySearch2(locations, name, minIndex, midIndex)
    elif name > mid[1]:
        return binarySearch2(locations, name, midIndex, maxIndex)


locations = readIn('Small.txt')
sort(locations)
locationName = input('Name of the location to search for: ')
indexFound = binarySearch2(locations, locationName, 0, len(locations))
if indexFound != None:
    print(locationName, 'is at index', indexFound)
else:
    print('That location was not found')
