def reverseString(s):
    str=""
    for i in s:
        str=i+str
        return str
    stringToReverse="String Reverse"
    print("Original string is:",stringToReverse)
    print("Reversed string is:",reverseString(stringToReverse))