import random as r
from math import sqrt


class Fish:
    def __init__(self):
        self.x = r.randint(0, 10)
        self.y = r.randint(0, 10)

    def move(self):
        self.x -= 1
        print("My position is: ", self.x, self.y)


class Goldfish(Fish):
    pass


class Carp(Fish):
    pass


class Salmon(Fish):
    pass


class Shark(Fish):
    def __init__(self):
        # Fish.__init__(self)
        super().__init__()
        self.hungry = True

    def eat(self):
        if self.hungry:
            print("My dream is eating everyday")
            self.hungry = False
        else:
            print("I;m full, can eat anymore")


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y


class Line:
    def __init__(self, p1, p2):
        self.x = p1.getX() - p2.getX()
        self.y = p1.getY() - p2.getY()

    def getLen(self):
        length = sqrt(self.x ** 2 + self.y ** 2)
        return length


class A:
    def __init__(self):
        print("Enter A")
        print("leave A")


class B(A):
    def __init__(self):
        print("Enter B")
        super().__init__()
        print("Leave B")


class C(A):
    def __init__(self):
        print("Enter C")
        super().__init__()
        print("Leave C")


class D(B,C):
    def __init__(self):
        print("Enter D")
        super().__init__()
        print("Leave D")


if __name__ == '__main__':
    fish = Fish()
    fish.move()
    goldfish = Goldfish()
    goldfish.move()
    shark = Shark()
    shark.move()
    shark.eat()
    shark.eat()
    p1 = Point(1, 1)
    p2 = Point(4, 5)
    line = Line(p1, p2)
    c = line.getLen()
    print(c)
    print("+" * 40)
    d = D()
