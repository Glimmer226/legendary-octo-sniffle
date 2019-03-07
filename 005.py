# -*- coding = utf-8 -*-
from math import sqrt

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y

class Line:
    def __init__(self, p1=0, p2=0):
        self.x = p1.getX() - p2.getX()
        self.y = p1.getY() - p2.getY()

    def getLen(self):
        len = sqrt(self.x ** 2 + self.y ** 2)
        print(len)



if __name__ == "__main__":
    p1 = Point(1, 1)
    p2 = Point(4, 5)
    line = Line(p1, p2)
    line.getLen()