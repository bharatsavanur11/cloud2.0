# Print hello 3 times for string manipulation things work differently in python
import string

#print("hello" * 3)


def getTriple(str: string):
    newstr = ''
    for char in str:
        for i in range(0, 3):
            newstr = newstr + char
    return [newstr, len(str)]


#print(getTriple('abc'))


def getStr1(s):
    s = s[:1] + s[0] + s[1:]  # Transform the string
    # Update the length of string
    strlen = len(s)
    return [s, strlen]


print(getStr1("abc"))
print(getStr1("xyz"))


## Find occurnces of b and ccc

def findOccurences(s):
    a = s.find('b')
    b = s.find('ccc')
    return [a,b]

print(findOccurences('aaabbccccc'))