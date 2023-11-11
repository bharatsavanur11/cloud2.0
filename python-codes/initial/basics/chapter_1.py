def MathOp():
    div = 3/2
    quotient = 3//2
    remainder = 3%2
    mult = 3**2
    return [div,quotient,remainder,mult]

[div,quot,rem,mult] = MathOp()

print(div)
print(quot)
print(rem)
print(mult)

#########
# Check parity

def checkParity(num):
    return num%2==0

print(checkParity(2))
print(checkParity(3))

# Print hello 3 times for string manipulaton things work differently in python
print("hello" * 3)

