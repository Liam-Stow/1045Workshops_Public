lstScores = []
fileScores = open('scores.txt')
for line in fileScores:
    line = line.split(' ')
    line[1] = int(line[1])
    line[2] = int(line[2])
    line[3] = int(line[3])
    line[4] = int(line[4])
    lstScores.append(line)
