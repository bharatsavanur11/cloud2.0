
class PersonService:
    _cache = str
    scientist_list = ["Aryabhatta India", "Newton UK", "Albert Einstein"]

    def __init__(self):
        self._cache = {}

    def __call__(self, personParam):
        if personParam not in self._cache:
            self._cache[personParam] = {personParam: 'test'}
        return self._cache[personParam]

    def is_test(self, name):
        if name in self._cache:
            return True
        else:
            return False

    ## Demoing Lambda Expressions Used.
    def sort_scientist(self):
        print(self.scientist_list)
        return sorted(self.scientist_list, key=lambda name: name.split()[-1])

    def build_person_info(name, **attributes):
        result = name + '=='
        for key, value in attributes.items():
            result = result + key + str(value)
        return result


class Calculate:

    def __init__(self):
        self._cache = {}

    def __call__(self):
        self.test = 10

    # Keyword args.
    def hyper_volume(self, *lengths):
        i = iter(lengths)
        v = next(i)
        for length in i:
            v = v * length
        return v

    # Local Functions.  factory Functions Closure
    def get_method_by_operation(operation_name: str, val1: int, val2: int):

        # Closure Variable
        mult_fact = 2

        def add():
            return (val1 + val2) * mult_fact

        def sub():
            return (val1 - val2) * mult_fact

        if operation_name == '+':
            return add
        else:
            return sub


# This is function level decorator used to do at a global level.
def smart_divide(func):
    def inner(a, b):
        print("I am being decorated")
        if b <= 0:
            b = 1

        return func(a, b)

    return inner


@smart_divide
def divide(a, b):
    return a / b


class MyDecorator:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print('I am being decorated')
        self.func(*args, **kwargs)
        print('Result after decoration')


@MyDecorator
def my_function(name: str):
    return name.capitalize()


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return self.name + "_" + str(self.age)
