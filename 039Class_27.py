class Test:
    count = 0

    def __init__(self):
        Test.count += 1
        print "Instance + %d" % Test.count

    def __del__(self):
        Test.count -= 1
        # print "Instance is %d" % Test.count


class Stack:
    def __init__(self):
        self.space = []

    def isEmpty(self):
        num = len(self.space)
        if num == 0:
            print 'Stack is empty'
        else:
            print 'Stack is not empty'

    def push(self, x):
        self.space.append(x)
        return self.space

    def pop(self):
        self.space.pop()
        return self.space[-1]

    def top(self):
        print self.space[-1]

    def bottom(self):
        print self.space[0]


class Word(str):
    def __new__(cls, word):
        if ' ' in word:
            print "Value contains paces. Truncating to first space."
            word = word[:word.index(' ')]
        return str.__new__(cls, word)

    def __gt__(self, other):
        return len(self) > len(other)

    def __lt__(self, other):
        return len(self) < len(other)

    def __ge__(self, other):
        return  len(self) >= len(other)

    def __le__(self, other):
        return  len(self) <= len(other)


class C:
    def __init__(self, *args):
        if not args:
            print "No args inputted"
        else:
            print "%d args have been inputted, they are" % len(args),
            for each in args:
                print each,


if __name__ == "__main__":
    a = Test()
    b = Test()
    c = Test()
    print Test.count
    del a
    print Test.count
    print "*" * 40
    stack = Stack()
    stack.isEmpty()
    stack.push('C')
    stack.push('h')
    stack.push('s')
    stack.push('i')
    stack.push('F')
    stack.top()
    stack.bottom()
    stack.pop()
    stack.top()
    stack.isEmpty()
    print "*" * 40
    c1 = C(1,2,3,4,5,6,7,8)