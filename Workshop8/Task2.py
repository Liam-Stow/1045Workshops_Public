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


locations = readIn('Small.txt')
printNicely(locations)
