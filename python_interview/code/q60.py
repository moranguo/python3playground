# 给定一个任意长度数组，实现一个函数
# 让所有奇数都在偶数前面，而且奇数升序排列，偶数降序排序，如字符串'1982376455',变成'1355798642'


def func1(l):
    # 如果传入的参数是字符串，转化为整数数组
    if isinstance(l,str):
        l = list(l)
        l = [int(i) for i in l]
    l.sort(reverse=True)
    for i in range(len(l)):
        if l[i] % 2>0:
            l.insert(0,l.pop(i))
    print(''.join(str(e) for e in l))


if __name__ == "__main__":
    func1("1982376455")
    func1([2, 4, 6, 7, 1, 2, 3, 4, 9, 0])
