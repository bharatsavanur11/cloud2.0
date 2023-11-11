# Concatenation
print([2, 3] + [5, 6])

val = [1, 3, 5, 7, 9]

for x in val:
    print(x)


def append(n):
    l = [1, 4, 9, 10, 23]
    l.append(n)
    # Alternate approach to do the same thing
    # l1 = l1 + [90]

    return l


print(append(90))


def average():
    l1 = [1, 4, 9, 10, 23]
    ## Write your code here
    avg = sum(l1) / len(l1)
    return avg


print(average())

# REMOVE THE DATA FROM LIST
# l1.remove(l2[0])
# l1.remove(l2[1])


### List Comprehensions #####

print([x * x for x in range(4)])

print([x * x * x for x in range(100) if (x % 10 == 0)])
