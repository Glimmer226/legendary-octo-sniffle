import random as r
from math import sqrt


class Ticket:
    def __init__(self, weekend=False, child=False):
        self.price = 100
        if weekend:
            self.coe = 1.2
        else:
            self.coe = 1
        if child:
            self.coech = 0.5
        else:
            self.coech = 1

    def calculate(self, num):
        return self.price * self.coe * self.coech * num


# Define the boundary of the game
scope_x = [0, 10]
scope_y = [0, 10]


class Turtle:
    def __init__(self):
        # initial the power
        self.power = 100
        # random the born position
        self.x = r.randint(scope_x[0], scope_x[1])
        self.y = r.randint(scope_y[0], scope_y[1])

    def move(self):
        # get the new position, moving random
        new_x = self.x + r.choice([1, 2, -1, -2])
        new_y = self.y + r.choice([1, 2, -1, -2])

        # check whether new position beyond the x boundary
        if new_x < scope_x[0]:
            self.x = scope_x[0] - (new_x - scope_x[0])
        elif new_x > scope_x[1]:
            self.x = scope_x[1] - (new_x - scope_x[1])
        else:
            self.x = new_x

        # check whether new position beyond the y boundary
        if new_y < scope_y[0]:
            self.y = scope_y[0] - (new_y - scope_y[0])
        elif new_y > scope_y[1]:
            self.y = scope_y[1] - (new_y - scope_y[1])
        else:
            self.y = new_y

        # power expend
        self.power -= 1

        # return the new position
        return self.x, self.y

    def eat(self):
        self.power += 20
        if self.power > 100:
            self.power = 100


class Fish:
    def __init__(self):
        # initial the random born position
        self.x = r.randint(scope_x[0], scope_x[1])
        self.y = r.randint(scope_y[0], scope_y[1])

    def move(self):
        # get the new position, moving random
        new_x = self.x + r.choice([1, -1])
        new_y = self.y + r.choice([1, -1])

        # check whether new position beyond the x boundary
        if new_x < scope_x[0]:
            self.x = scope_x[0] - (new_x - scope_x[0])
        elif new_x > scope_x[1]:
            self.x = scope_x[1] - (new_x - scope_x[1])
        else:
            self.x = new_x

        # check whether new position beyond the y boundary
        if new_y < scope_y[0]:
            self.y = scope_y[0] - (new_y - scope_y[0])
        elif new_y > scope_y[1]:
            self.y = scope_y[1] - (new_y - scope_y[1])
        else:
            self.y = new_y

        return self.x, self.y


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getx(self):
        return self.x

    def gety(self):
        return self.y


class Line:
    def __init__(self, p1, p2):
        self.x = p1.getx() - p2.getx()
        self.y = p1.gety() - p2.gety()

    def getl(self):
        length = sqrt(self.x ** 2 + self.y ** 2)
        return length


class A:
    def __init__(self):
        print "Enter A"
        print "Leave A"


class B(A):
    def __init__(self):
        print "Enter B"
        super(B, self).__init__()
        print "Leave B"


class C(A):
    def __init__(self):
        print "Enter C"
        super(C, self).__init__()
        print "Leave C"


class D(B, C):
    def __init__(self):
        print "Enter D"
        super(D, self).__init__()
        print "Leave D"


if __name__ == "__main__":
    adult = Ticket()
    child = Ticket(child=True)
    print "The price should be %s " % str(adult.calculate(2) + child.calculate(1))
    print "+" * 40

    turtle = Turtle()
    fish = []
    for i in range(10):
        new_fish = Fish()
        fish.append(new_fish)

    while True:
        if not len(fish):
            print "All fish have been ate, game over"
            break
        if not turtle.power:
            print "Turtle have out of power, game over"
            break

        pos = turtle.move()

        for each_fish in fish[:]:
            if each_fish.move() == pos:
                # fish have been ate
                turtle.eat()
                fish.remove(each_fish)
                print "A fish have been ate"

    print "+" * 40

    try:
        p1 = Point(1, 1)
        p2 = Point(4, 5)
        line = Line(p1, p2)
        print line.getl()
    except Exception as e:
        print e

    print "+" * 40
    b = B()