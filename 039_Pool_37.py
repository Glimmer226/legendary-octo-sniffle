class Turtle:
    def __init__(self, x):
        self.num = x


class Fish:
    def __init__(self, x):
        self.num = x


class Pool:
    def __init__(self, x, y):
        self.turtle = Turtle(x)
        self.fish = Fish(y)

    def print_num(self):
        print("There are %d turtle and %d fish in the pool" % (self.turtle.num, self.fish.num))


class Test:
    count = 0

    def __init__(self):
        Test.count += 1
        # print("Class number is %d" % Test.count)

    def __del__(self):
        Test.count -= 1


class Stack:
    def __init__(self, start=[]):
        self.stack = []
        for x in start:
            self.push(x)

    def isEmpty(self):
        return not self.stack

    def push(self, y):
        self.stack.append(y)

    def pop(self):
        if not self.stack:
            print("Warning: Stack is empty!")
        else:
            return self.stack.pop()

    def top(self):
        if not self.stack:
            print("Warning: Stack is empty!")
        else:
            return self.stack[-1]

    def buttom(self):
        if not self.stack:
            print("Warning: Stack is empty!")
        else:
            return self.stack[0]


if __name__ == "__main__":
    pool = Pool(1, 10)
    pool.print_num()
    a = Test()
    b = Test()
    c = Test()
    print(Test.count)
    del c
    print(Test.count)
    print("#" * 40)
    stack = Stack([5, 6, 7, 8])
    stack.top()
    stack.buttom()
    stack.pop()
    stack.push(0)
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(stack.top())
    print(stack.buttom())
    print(stack.pop())