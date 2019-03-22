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


if __name__ == "__main__":
    c = C2F(32)
    print(c)
    print(Nint(123))
    print(Nint(1.5))
    print(Nint("abc"))