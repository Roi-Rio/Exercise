# -*- coding: UTF-8 -*-
def separation(func):
    print('——' * 30)
    print(func.__doc__)
    print('——' * 30)
    func()
    print('——' * 30)
def _005():
    """005 输入三个整数x,y,z，请把这三个数由小到大输出。"""
    lis = []
    for i in range(3):
        lis.append(int(input('输入一个整数：')))
    lis.sort()
    print('排序后为：', lis)
def _006():
    """006 斐波那契数列。输出0、1、1、2、3、5、8、13、21、34、……。"""
    def fib(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return fib(n-1) + fib(n-2)
    x = int(input('输入需要的个数：'))
    for i in range(x):
        print(fib(i), end=' ')
    print()
def _007():
    """007 将一个列表的数据复制到另一个列表中。"""
    x = input('输入一个列表：')
    lis = x.split(',')
    for i, s in enumerate(lis):
        lis[i] = int(s)
    print('输入的列表为：', lis)
    lis2 = lis[:]
    print('新的列表为：', lis2)
def _008():
    """008 输出 9*9 乘法口诀表。"""
    for i in range(1, 10):
        for j in range(1, 10):
            if i >= j:
                print('{}×{}={:<2d}'.format(j, i, i*j), end=' ')
        print()


separation(_008)
