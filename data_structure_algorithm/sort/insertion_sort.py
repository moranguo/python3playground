def insertion_sort(my_list):
    n = len(my_list)
    if n <= 1:
        return

    for i in range(1, n):
        value = my_list[i]
        j = i - 1
        # 查找插入的位置
        while j >= 0 and my_list[j] > value:
            my_list[j + 1] = my_list[j]  # 数据移动
            j -= 1
        my_list[j + 1] = value  # 插入数据


if __name__ == "__main__":
    a = [4, 5, 6, 3, 2, 1]
    b = [3, 5, 4, 1, 2, 6]
    c = [1, 2, 3, 4, 5, 6]
    print('before sort', a)
    print('before sort', b)
    print('before sort', c)
    insertion_sort(a)
    insertion_sort(b)
    insertion_sort(c)
    print('after sort', a)
    print('after sort', b)
    print('after sort', c)
