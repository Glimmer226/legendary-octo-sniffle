class CountList:
    def __init__(self, *args):
        self.values = [x for x in args]
        self.count = {}.fromkeys(range(len(self.values)), 0)

    def __len__(self):
        return len(self.values)

    def __getitem__(self, item):
        self.count[item] += 1
        return self.values[item]


class CountList1(list):
    def __init__(self, *args):
        super().__init__(args)
        self.count = []
        for i in args:
            self.count.append(0)

    def __len__(self):
        return len(self.count)

    def __getitem__(self, item):
        self.count[item] += 1
        return super().__getitem__(item)

    def __setitem__(self, key, value):
        self.count[key] += 1
        super().__setitem__(key, value)

    def __delitem__(self, key):
        del self.count[key]
        super().__delitem__(key)

    def counter(self, key):
        return self.count[key]

    def append(self, value):
        self.count.append(0)
        super().append(value)

    def pop(self, key=-1):
        del self.count[key]
        return super().pop(key)

    def remove(self, value):
        key = super().index(value)
        del self.count[key]
        super().remove(value)

    def insert(self, key, value):
        self.count.insert(key, 0)
        super().insert(key, value)

    def clear(self):
        self.count.clear()
        super().clear()

    def reverse(self):
        self.count.reverse()
        super().reverse()


if __name__ == "__main__":
    a = CountList(1, 3, 5, 7, 9)
    b = CountList(2, 4, 6, 8, 10)
    print(a[1])
    print(b[1])
    print(a[1] + b[1])
    print(a.count)
