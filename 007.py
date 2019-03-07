# -*- coding = utf-8 -*-


import time


class FileObject:
    """给文件对象进行包装从而确认在删除文件时文件流关闭"""

    def __init__(self, filename='sample.txt'):
        # 读写模式打开一个文件
        self.new_file = open(filename, 'r+')

    def __del__(self):
        self.new_file.close()
        del self.new_file


class C2F(float):
    """摄氏度转为华氏度"""
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


if __name__ == '__main__':
    print(C2F(32))
    print(Nint('FishC'))
