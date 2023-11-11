class PersonClass:
    def __init__(self, name, age):
        self.age = age
        self.name = name

    def greet(self):
        print('My name is %s' % self.name)


a = PersonClass("Ananya", 8)

a.greet()


class Rectangle:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def width(self):
        return self.x2 - self.x1

    def height(self):
        return self.y2 - self.y1
    def area(self):
        return self.width() * self.height()

    def __repr__(self):
        return str(self.x1) + ',' + str(self.x2)


r = Rectangle(1, 2, 3, 4)
print(r)
print(r.area())


class TenYearOldPersonClass(PersonClass):
    def __init__(self, name):
        # No need to pass self in the super class
        super().__init__(name, 20)

    def greet(self):
        print("I am calling from child class")


t = TenYearOldPersonClass("Ananya")

print(t.name)
