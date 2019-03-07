# -*- coding = utf-8 -*-
import easygui as g


class Person:
    name = "FishC"

    def func(self):
        print(self.name)

class Rectangle:
    length = 0
    width = 0

    def setRect(self):
        result = g.multenterbox("Please enter the Length and Width as you want", "Rectangle", ['Length', 'Width'])
        self.length = float(result[0])
        self.width = float(result[1])
        #print(self.length)
        #print(self.width)

    def getRect(self):
        msg = "The Length is: %.2f, Width is: %.2f" % (self.length, self.width)
        title = "Rectangle"
        g.msgbox(msg, title)

    def getArea(self):
        area = self.length * self.width
        #print(area)
        g.msgbox("The area is %.2f" % area, "Rectangle")



if __name__ == '__main__':
    #p = Person()
    #p.func()
    p = Rectangle()
    p.setRect()
    p.getArea()
    p.getArea()