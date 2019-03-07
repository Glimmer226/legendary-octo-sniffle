# -*- coding = utf-8 -*-


class Stack:
    def __init__(self):
        self.stack = []

    def isEmpty(self):
        return not self.stack

    def pop(self):
        try:
            self.stack.remove(self.stack[-1])
            return self.stack
        except IndexError:
            print('Stack is empty')

    def push(self, x):
        self.stack.append(x)
        return self.stack

    def top(self):
        try:
            print(self.stack[-1])
        except IndexError:
            print("Stack is empty")

    def bottom(self):
        try:
            print(self.stack[0])
        except IndexError:
            print("Stack is empty")


if __name__ == "__main__":
    s = Stack()
    s.push(1)
    s.top()
    s.push(1)
    s.bottom()