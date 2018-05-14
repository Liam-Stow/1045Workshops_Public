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

inputStr = input("Please input a string to test if it is a palindrome: ").lower()
if isPalindrome((inputStr.lower())):
    print("Great, this sentence is a palindrome")
else:
    print("Unfortunately, this sentence is not a palindrome")
