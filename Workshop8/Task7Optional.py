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


#Partition towns around an input town in alphabetical order
def partitionTowns(locations, position):
    beforeS = []
    afterS = []

    for location in range(0, position)
        beforeS.append(locations[location])
        
    for location in range(position+1, len(locations)):
        afterS.append(locations[location])

    
    
    
locations = readIn('Small.txt')
sort(locations)
print('Index Code Town')
print('---------------')
printNicely(locations)

pivotIndex = int(input('Select an index of the list: '))

partitionTowns(locations, pivotIndex)

