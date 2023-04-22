
from basics.NumberGenerator import PrintNumber
from basics.NumberGenerator import mul
from basics.NumberGenerator import add
from basics.NumberGenerator import add1

p1 = Person("AA", 20)
p2 = Person("BB", 10)
p3 = Person("CC", 15)
p4 = Person("CC", 15)

# defining custom list
p = [p1, p2, p3]
# sorting immuability
sorted(p, key=lambda per: per.age)

print(p)

# sorting data
# print(sorted(p, key=lambda per: per.age))

# Running While Loop
i1 = 1
while i1 < len(p):
    # print(i1)
    i1 = i1 + 1

# set is different from java and doesn't work.
## s = set[p1, p2, p3, p4]
## print('Size', s.__sizeof__())

# Custom iterator
p_num = PrintNumber(40)
print(set(p_num))

# for i in p_num:
# print(i)

# iter(p_num)

l = [1, 2, 3, 4, 5]

#Lambda and collection test. Works slightly different in
# python compared to java as it is immutable and a new collection is created everytime.
print("Map test")
print(list(map(lambda x: add1(x), l)))
print(list(filter(lambda x: x > 4, l)))
