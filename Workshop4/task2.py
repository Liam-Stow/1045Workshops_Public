def isPalindrome(string):
    if len(string) == 0:
        return False
    for char in string:
        if char in ' ,.?':
            string = string.replace(char,"")
    string2 = string[::-1]
    if string2 == string:
        return True
    return False

palFile = open('palindromic.txt')
for line in palFile:
    line = line.split(' ')
    line = "".join(line)
    line = line.strip('\n')
    if isPalindrome(line):
        print("%s is a palindrome" % (line))
    else:
        print("%s is not a palindrome" % (line))
