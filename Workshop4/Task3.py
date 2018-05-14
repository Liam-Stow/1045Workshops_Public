

'''WORKSHOP 4 TASK 3'''


#Open text file
dataFile = open('Tides.txt')

#Determine first date in file
firstDate = dataFile.readline()
firstDate = firstDate.split(',')[0]
prevDate = firstDate

#Create data structure
day = []
dataList = []
for line in dataFile:

    #Decode line
    line = line.strip('meters \n')
    moment = line.split(',')
    
    #Seperate days
    date = moment[0]
    if date != prevDate:
        dataList.append(day)
        day = []
        day.append(moment)
    else:
        day.append(moment)

    prevDate = date


#Create table to hold highs and lows
records = []
'''
would hold:
[
    [date, highestTime, highest, lowestTime, lowest],
    [date, highestTime, highest, lowestTime, lowest],
    ... ]
]
'''

#Find the lowest and highest moments
for day in dataList:
    
    lowest = float(day[0][2])
    lowestTime = 0
    highest = float(day[0][2])
    highestTime = 0
    
    for moment in day:
        if float(moment[2]) > highest:
            highest     = float(moment[2])
            highestTime = float(moment[1])
        if float(moment[2]) < lowest:
            lowest      = float(moment[2])
            lowestTime  = float(moment[1])
    records.append([day[0][0], highestTime, highest, lowestTime, lowest])
    print("{}: {} meters at lowest and {} meters at highest".format(day[0][0], lowest, highest))


#Calculate the average time for low and high tide
highestTimeSum = 0
lowestTimeSum = 0
for day in records:
    highestTimeSum += day[1]
    lowestTimeSum += day[3]
noOfRecords = len(records)
highestTimeAve = highestTimeSum/noOfRecords
lowestTimeAve = lowestTimeSum/noOfRecords

print('\n')
print('Over the full period, on average the lowest and highest tides occured at {:.2f} and {:.2f} hours after midnight'.format(highestTimeAve, lowestTimeAve))
