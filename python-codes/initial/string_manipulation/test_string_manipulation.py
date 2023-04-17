
firstnanme = 'AAA BBB CCC DDDD'.split(' ')[0]
# print(firstnanme)

x = {'sss': 'sss@gmail.com', 'bbbb': 'bbbb.gamil.com'}

for keys in x.keys():
    print(keys)

# Tuple Example

x = {'aaa', 'bbb', 'aaa.bbb@gmail.com'}

(first_name, last_name, email) = x

print(last_name)
print(email)

# list compprehension

my_list = [number for number in range(0 ,20) if number % 2 ==0]

print(my_list)

sum_val = sum([number for number in range(0 ,20) if number % 2 ==0])
print(sum_val)