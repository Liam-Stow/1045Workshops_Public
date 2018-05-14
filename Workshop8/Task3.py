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


locations = readIn('Small.txt')
sort(locations)
printNicely(locations)
