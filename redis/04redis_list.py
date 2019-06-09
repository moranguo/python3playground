import redis
import time

pool = redis.ConnectionPool(host='localhost', port=6379, decode_responses=True)
r = redis.Redis(connection_pool=pool)
# clear all data in redis
r.flushdb()


r.lpush("list1", 11, 22, 33)
print(r.lrange('list1', 0, -1))

r.rpush("list2", 11, 22, 33)  # 表示从右向左操作
print(r.llen("list2"))  # 列表长度
print(r.lrange("list2", 0, 3))  # 切片取出值，范围是索引号0-3

r.rpush("list2", 44, 55, 66)    # 在列表的右边，依次添加44,55,66
print(r.llen("list2"))  # 列表长度
print(r.lrange("list2", 0, -1)) # 切片取出值，范围是索引号0到-1(最后一个元素)

r.lpushx("list10", 10)   # 这里list10不存在
print(r.llen("list10"))  # 0
print(r.lrange("list10", 0, -1))  # []

r.lpushx("list2", 77)   # 这里"list2"之前已经存在，往列表最左边添加一个元素，一次只能添加一个
print(r.llen("list2"))  # 列表长度
print(r.lrange("list2", 0, -1)) # 切片取出值，范围是索引号0到-1(最后一个元素

r.rpushx("list2", 99)   # 这里"foo_list1"之前已经存在，往列表最右边添加一个元素，一次只能添加一个
print(r.llen("list2"))  # 列表长度
print(r.lrange("list2", 0, -1)) # 切片取出值，范围是索引号0到-1(最后一个元素)

r.linsert("list2", "before", "11", "00")   # 往列表中左边第一个出现的元素"11"前插入元素"00"
print(r.lrange("list2", 0, -1))   # 切片取出值，范围是索引号0-最后一个元素

r.lset("list2", 0, -11)    # 把索引号是0的元素修改成-11
print(r.lrange("list2", 0, -1))

# lrem key count value
r.lrem("list2", 1, "11")    # 将列表中左边第一次出现的"11"删除
print(r.lrange("list2", 0, -1))
r.lrem("list2", -1, "99")    # 将列表中右边第一次出现的"99"删除
print(r.lrange("list2", 0, -1))
r.lrem("list2", 0, "22")    # 将列表中所有的"22"删除
print(r.lrange("list2", 0, -1))

r.lpop("list2")    # 删除列表最左边的元素，并且返回删除的元素
print(r.lrange("list2", 0, -1))
r.rpop("list2")    # 删除列表最右边的元素，并且返回删除的元素
print(r.lrange("list2", 0, -1))

r.ltrim("list2", 0, 2)    # 删除索引号是0-2之外的元素，值保留索引号是0-2的元素
print(r.lrange("list2", 0, -1))

print(r.lindex("list2", 0))  # 取出索引号是0的值

r.rpoplpush("list1", "list2")
print(r.lrange("list2", 0, -1))

r.brpoplpush("list1", "list2", timeout=2)
print(r.lrange("list2", 0, -1))

r.lpush("list10", 3, 4, 5)
r.lpush("list11", 3, 4, 5)
while True:
    r.blpop(["list10", "list11"], timeout=2)
    print(r.lrange("list10", 0, -1), r.lrange("list11", 0, -1))
    if r.llen("list11") == 0:
        break

# 自定义增量迭代
# 由于redis类库中没有提供对列表元素的增量迭代，如果想要循环name对应的列表的所有元素，那么就需要：
#
# 获取name对应的所有列表
# 循环列表
#
# 但是，如果列表非常大，那么就有可能在第一步时就将程序的内存撑爆，所有有必要自定义一个增量迭代的功能：
def list_iter(name):
    """
    自定义redis列表增量迭代
    :param name: redis中的name，即：迭代name对应的列表
    :return: yield 返回 列表元素
    """
    list_count = r.llen(name)
    for index in range(list_count):
        yield r.lindex(name, index)

# 使用
for item in list_iter('list2'): # 遍历这个列表
    print(item)
