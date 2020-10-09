def selection_sort(my_list):
    n = len(my_list)
    if n <= 1:
        return

    for i in range(n):
        min_index = i
        min_value = my_list[i]
        for j in range(i, n):
            if my_list[j] < min_value:
                min_value = my_list[j]
                min_index = j
        tmp = my_list[i]
        my_list[i] = my_list[min_index]
        my_list[min_index] = tmp


if __name__ == "__main__":
    a = [4, 5, 6, 3, 2, 1]
    b = [3, 5, 4, 1, 2, 6]
    c = [1, 2, 3, 4, 5, 6]
    print('before sort', a)
    print('before sort', b)
    print('before sort', c)
    selection_sort(a)
    selection_sort(b)
    selection_sort(c)
    print('after sort', a)
    print('after sort', b)
    print('after sort', c)
