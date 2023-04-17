i = ['a','b','c']+[1,2,3]
print(i)



# Custom Iterator
class PrintNumber:
    def __init__(self, max_num):
        self.max_num = max_num

    def __iter__(self):
        self.num = 0
        return self

    def __next__(self):
        if self.num > self.max_num:
            # Raise an Exception and stop the iteration
            raise StopIteration
        print(self.num)
        self.num += 1
        return self.num


def mul(x, y):
    return x * y


def add(x, y):
    return x + y


def add1(x):
    return x + x
