file = open('Small.txt')
locations = []

for line in file:
    line = line.strip()

    #Split postcode from string
    line = line.split('\t')
    postcode = int(line[0])

    #Split towns appart
    line[1] = line[1].split(',')
    for place in line[1]:
        locations.append([postcode, place])

print(locations)
