def output_letter(letter):
    l = []
    for item in letter:
        l.append(item)
    return l


def output_letter2(letter):
    return [l for l in letter]


def output_letter3(letter):
    return [l for l in letter if 'k' in l]


def square(l):
    square_list = []
    for ele in l:
        square_list.append(ele * ele)
    return square_list


a = lambda l: [item*item for item in l]


if __name__ == "__main__":
    # print(output_letter('kevin'))
    # print(output_letter('kevin'))
    # print(output_letter3(['kevin', 'Eric', 'hello']))

    # print(square([1, 2, 3, 4]))
    # print(a([1, 2, 3, 4]))

    # type(obj)返回对象类型
    # print(type(7), type(2.0), type(int))
    # type() 常常跟函数isinstance() 配合使用，用来检测一个变量是否是我们需要的类型
    # x = 6
    # if isinstance(x, int):
    #     print('I am an int')

    # # dir() 可以用来获取当前模块的属性列表，也可以获取指定一个属性。
    # my_list = [1, 2, 3]
    # print(dir(my_list))
    # print(dir(my_list).__class__)

    # # id()函数返回对象的唯一标识符
    # name = "kevin"
    # alias_name = name
    # another_name = "kevin"
    # # 以下所列的唯一标识符都是一样的，例如2191393817584 2191393817584 2191393817584
    # print(id(name), id(alias_name), id(another_name))

    