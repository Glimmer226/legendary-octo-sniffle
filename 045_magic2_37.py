class Rectangle:
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    def __setattr__(self, key, value):
        if key == 'square':
            self.width = value
            self.height = value
        else:
            super().__setattr__(key, value)
            # self.__dict__[key] = value

    def getArea(self):
        return self.width * self.height


class A:
    def __getattr__(self, item):
        return "This attribute dose not exist"


class Demo:
    def __getattr__(self, item):
        self.item = 'FishC'
        return self.item


class Counter:
    def __init__(self):
        super().__setattr__('counter'', 0)

    def __setattr__(self, key, value):
        super.__setattr__('counter', self.counter + 1)
        super.__setattr__(key, value)

    def __delattr__(self, item):
        super().__setattr__('counter', self.counter - 1)
        super().__delattr__(item)


if __name__ == "__main__":
    '''r1 = Rectangle(4, 5)
    r1.square = 10
    print(r1.width)
    print(r1.height)
    print(r1.getArea())
    print(r1.__dict__)'''

    # a = A()
    # print(a.x)

    demo = Demo()
    print(demo.x)
    demo.x = "X-man"
    print(demo.x)
    c = Counter()
    c.x = 1
    print(c.counter)