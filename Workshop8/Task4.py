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


#Find the postcode of a location, given its name
def binarySearch(locations,name):
    low = 0    
    high =len(locations)-1
    
    while low <= high:
        mid=(low + high)//2
        if locations[mid][1]==name:
            return locations[mid][0]
        elif locations[mid][1]>name:
            high = mid-1
        else:
            low = mid+1

fileName = input('Enter name of postcode file: ')
locations = readIn(fileName)
sort(locations)
suburbName = input('Enter Suburb Name: ')
postcode = binarySearch(locations, suburbName)
if postcode:
    print('Post code is', postcode)
else:
    print('Could not find that location')
