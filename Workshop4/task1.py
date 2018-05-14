def isPalindrome(string):
    string2 = string[::-1]
    if string2 == string:
        return True
    return False

inputStr = input("Please input a string to test if it is a palindrome: ")
if isPalindrome((inputStr.lower())):
    print("Great, %s is a palindrome" % (inputStr))
else:
    print("Unfortunately, %s is not a palindrome" % (inputStr))
