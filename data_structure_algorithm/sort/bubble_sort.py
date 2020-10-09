def bubble_sort(my_list):
    n = len(my_list)
    if n <= 1:
        return
    for i in range(n):
        # 提前退出冒泡循环的标志位
        flag = False
        # range(0)不会产生元素
        for j in range(n-i-1):
            if my_list[j] > my_list[j+1]:  # 交换
                tmp = my_list[j]
                my_list[j] = my_list[j+1]
                my_list[j + 1] = tmp
                flag = True  # 表示有数据交换
        if not flag:  # 没有数据交换，提前退出
            break


if __name__ == "__main__":
    a = [4, 5, 6, 3, 2, 1]
    b = [3, 5, 4, 1, 2, 6]
    print('before sort', a)
    print('before sort', b)
    bubble_sort(a)
    bubble_sort(b)
    print('after sort', a)
    print('after sort', b)

    c = [3, 5, 4, 1, 2, 6]
    print('before sort', c)
    c.sort()
    print('after sort', c)
