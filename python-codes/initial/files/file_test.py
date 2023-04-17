# The path to file in python start from the directory where ur
# python file is located.
with open('files/test_data.txt', 'r') as reader:
    print(reader.read())

# read line by line
with open('files/test_data.txt', 'r') as reader:
    line = reader.readline()
    while line != '':
        print(line)
        line = reader.readline()
