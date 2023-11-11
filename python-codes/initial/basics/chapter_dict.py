# how to create dictionary and iterate over it
ages = {
    "bharat": 37,
    "anusha": 36
}

print(ages)

for name, age in ages.items():
    print(name + "_" + str(age))

s = {1, 2, 3}

booltw = s.add(4)

print(booltw)

for x in ages:
    print(ages[x])

for name, age in ages.items():
    print(name, age)


def oldestStudent(ages):
    value = list(ages.values())
    key = list(ages.keys())
    return key[value.index(max(value))]


ages = {
    "Peter": 10,
    "Isabel": 11,
    "Anna": 9,
    "Thomas": 10,
    "Bob": 10,
    "Joseph": 11,
    "Maria": 12,
    "Gabriel": 10,
}
print(oldestStudent(ages))
