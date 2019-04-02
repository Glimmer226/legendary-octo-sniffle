class FileObject:
    def __init__(self, filename='simple.txt'):
        self.new_file = open(filename, 'r+')

    def __del__(self):
        self.new_file.close()
        del self.new_file


class C2F(float):
    def __new__(cls, arg=0.0):
        return float.__new__(cls, arg * 1.8 + 32)


class Nint(int):
    def __new__(cls, arg=0):
        if isinstance(arg, str):
            total = 0
            for each in arg:
                total += ord(each)
            arg = total
        return int.__new__(cls, arg)


class Nstr(str):
    def __sub__(self, other):
        return self.replace(other, ' ')


class Bstr(str):
    def __lshift__(self, other):
        return self[other:] + self[:other]

    def __rshift__(self, other):
        return self[:-other] + self[-other:]


class Cstr:
    def __init__(self, arg=''):
        if isinstance(arg, str):
            self.total = 0
            for each in arg:
                self.total += ord(each)
        else:
            print("Wrong parameters")

    def __add__(self, other):
        return self.total + other.total

    def __sub__(self, other):
        return  self.total - other.total

    def __mul__(self, other):
        return self.total * other.total

    def __truediv__(self, other):
        return self.total / other.total

    def __floordiv__(self, other):
        return self.total // other.total


class C:
    @staticmethod
    def static(arg1, arg2, arg3):
        print(arg1, arg2, arg3)

    def nostatic(self):
        print("I'm the normal method!")


class D:
    def __init__(self, *args):
        if not args:
            print("No args input")
        else:
            print("%d args have been inputted, each is:" % len(args))
            for each in args:
                print(each, end=' ')


class Word(str):
    def __new__(cls, word):
        if ' ' in word:
            print("Value contains spaces. Truncating to first space.")
            word = word[:word.index(" ")]
        return str.__new__(cls, word)

    def __lt__(self, other):
        return len(self) < len(other)

    def __gt__(self, other):
        return len(self) > len(other)

    def __ge__(self, other):
        return len(self) >= len(other)

    def __le__(self, other):
        return len(self) <= len(other)


if __name__ == "__main__":
    c = C2F(32)
    print(c)
    print(Nint(123))
    print(Nint(1.5))
    print(Nint("abc"))
    a = Nstr("I love FishC.com! iiiiiii")
    b = Nstr("i")
    print(a - b)
    c = Bstr('I love FishC.com!')
    print(c << 3)
    print(c >> 3)
    d = Cstr('FishC')
    e = Cstr("love")
    print(d + e)
    print(d - e)
    print(d * e)
    print(d / e)
    print(d // e)
    print("*" * 50)
    c1 = C()
    c2 = C()
    print(c1.static is C.static)
    print(c1.nostatic is C.nostatic)
    print(c1.static)
    print(c2.static)
    print(C.static)
    print(c1.nostatic)
    print(c2.nostatic)
    print(C.nostatic)
    print(c1.static(1, 2, 3))
    print(C.static(1, 2, 3))
    print("*" * 50)
    d = D(12,3,4,5,6,7,8,98,90,0)
