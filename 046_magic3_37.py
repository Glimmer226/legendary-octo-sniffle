import time
import os
import pickle


class Celsius:
    def __init__(self, value=26.0):
        self.value = float(value)

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        self.value = float(value)


class Fahrenheit:
    def __get__(self, instance, owner):
        return instance.cel * 1.8 + 32

    def __set__(self, instance, value):
        instance.cel = (float(value) - 32) / 1.8


class Temperature:
    cel = Celsius()
    fah = Fahrenheit()


class MyDes:
    def __init__(self, value=0):
        self.val = value

    def __get__(self, instance, owner):
        return self.val - 20

    def __set__(self, instance, value):
        self.val = value + 10
        print(self.val)


class C:
    x = MyDes()


class MyDes1:
    def __init__(self, value = None):
        self.val = value

    def __get__(self, instance, owner):
        return self.val ** 2


class Test:
    # def __init__(self):
    #     self.x = MyDes1(3)
    x = MyDes1(3)


class MyDes2:
    def __get__(self, instance, owner):
        print("getting....")


class Test1:
    a = MyDes2()
    x = a


class MyDes3:
    def __init__(self, initval=None, name=None):
        self.val = initval
        self.name = name

    def __get__(self, instance, owner):
        print("Getting the variable: ", self.name)
        return self.val

    def __set__(self, instance, value):
        print("Setting the variable: ". self.name)
        self.val = value

    def __delete__(self, instance):
        print("Deleting the variable: ", self.name)
        print("Oh, this variable can't be delete")


class Record:
    def __init__(self, value, name):
        self.val = value
        self.name = name

    def __get__(self, instance, owner):
        with open("Property.txt", "a+") as f:
            f.write("%s 变量于北京时间 %s 被读取，%s = %s\n" % (self.name, time.asctime(), self.name, str(self.val)))
        return self.val

    def __set__(self, instance, value):
        with open("Property.txt", "a+") as f:
            f.write("%s 变量于北京时间 %s 被修改， %s = %s\n" % (self.name, time.asctime(), self.name, str(self.val)))
        self.val = value


class Test2:
    x = Record(10, 'x')
    y = Record(8.8, "y")


class MyDes4:
    saved = []

    def __init__(self, name = None):
        self.name = name
        self.filename = self.name + '.pkl'

    def __get__(self, instance, owner):
        if self.name not in MyDes4.saved:
            raise AttributeError("%s 属性还没有赋值！" % self.name)
        with open(self.filename, 'rb') as f:
            value = pickle.load(f)
        return value

    def __set__(self, instance, value):
        with open(self.filename, 'wb') as f:
            pickle.dump(value, f)
            MyDes4.saved.append(self.name)

    def __delete__(self, instance):
        os.remove(self.filename)
        MyDes4.saved.remove(self.name)


class Test3:
    x = MyDes4('x')
    y = MyDes4('y')


if __name__ == "__main__":
    temp = Temperature()
    print(temp.cel)
    temp.cel = 30
    print(temp.cel)
    temp.fah = 100
    print(temp.cel)
    print("*" * 40)
    c = C()
    # print(c.x)
    c.x = 10
    print(c.x)
    print("*" * 40)
    test = Test()
    print(test.x)
    print("*" * 40)
    test1 = Test1()
    print("*" * 40)
    test2 = Test2()
    print(test2.x)
    test2.y
    test2.x = 123
    test2.x = 1.23
    test2.y = "I love FishC.com"
    print("*" * 40)
    test3 = Test3()
    test3.x = 123
    test3.y = "I love FishC.com!"
    print(test3.x)
    print(test3.y)
    del test3.x