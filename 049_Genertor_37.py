import math
import sys


def myRev(data):
    # 这里用range生成data的倒叙索引
    # 注意，range的结束位置是不包含的
    for index in range(len(data)-1, -1, -1):
        yield data[index]


def is_prime(number):
    if number > 1:
        if number == 2:
            return True
        if number % 2 == 0:
            return False
        for current in range(3, int(math.sqrt(number) + 1), 2):
            if number % current == 0:
                return False
        return True
    return False


def get_prime(number):
    while True:
        if is_prime(number):
            yield number
        number += 1


def solve():
    total = 2
    for next_prime in get_prime(3):
        if next_prime < 2000000:
            total += next_prime
        else:
            print(total)


class Const:
    def __setattr__(self, key, value):
        if key in self.__dict__:
            raise TypeError("常量无法改变!")

        if not key.isupper():
            raise TypeError("常量名必须由大写字母组成！")

        self.__dict__[key] = value


sys.modules[__name__] = Const()


if __name__ == "__main__":
    for i in myRev("FishC"):
        print(i, end='')

    solve()
    