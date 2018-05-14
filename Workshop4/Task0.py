#read in file
file = open("mod_haiku.txt")
origHiaku = file.readline()
file.close()

#Define replacement characters
space = " "
newLine = "\n"

#Split the string into a list of lines
newHiaku = origHiaku.split("\t")

#Split each line into words
length = len(newHiaku)
for lineIndex in range(length):
    newHiaku[lineIndex] = newHiaku[lineIndex].split(";")

    #patch words back together with spaces
    newHiaku[lineIndex] = space.join(newHiaku[lineIndex])

#patch lines back together with newlines
newHiaku = newLine.join(newHiaku)


print(newHiaku)
