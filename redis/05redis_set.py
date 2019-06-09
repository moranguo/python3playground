import redis

pool = redis.ConnectionPool(host='localhost', port=6379, decode_responses=True)
r = redis.Redis(connection_pool=pool)

r.sadd("set1", 33, 44, 55, 66)  # 往集合中添加元素
print(r.scard("set1"))  # 集合的长度是4
print(r.smembers("set1"))   # 获取集合中所有的成员

# 获取集合中所有的成员--元组形式
# sscan(name, cursor=0, match=None, count=None)
print(r.sscan("set1"))

# 获取集合中所有的成员--迭代器的方式
# sscan_iter(name, match=None, count=None)
# 同字符串的操作，用于增量迭代分批获取元素，避免内存消耗太大
for i in r.sscan_iter("set1"):
    print(i)

r.sadd("set2", 11, 22, 33)
print(r.smembers("set1"))   # 获取集合中所有的成员
print(r.smembers("set2"))
print(r.sdiff("set1", "set2"))   # 在集合set1但是不在集合set2中
print(r.sdiff("set2", "set1"))   # 在集合set2但是不在集合set1中

r.sdiffstore("set3", "set1", "set2")    # 在集合set1但是不在集合set2中
print(r.smembers("set3"))   # 获取集合3中所有的成员

print(r.sinter("set1", "set2")) # 取2个集合的交集

print(r.sinterstore("set3", "set1", "set2")) # 取2个集合的交集
print(r.smembers("set3"))

print(r.sunion("set1", "set2")) # 取2个集合的并集

print(r.sunionstore("set3", "set1", "set2")) # 取2个集合的并集
print(r.smembers("set3"))

print(r.sismember("set1", 33))  # 33是集合的成员
print(r.sismember("set1", 23))  # 23不是集合的成员

r.smove("set1", "set2", 44)
print(r.smembers("set1"))
print(r.smembers("set2"))

print(r.spop("set2"))   # 这个删除的值是随机删除的，集合是无序的
print(r.smembers("set2"))

print(r.srem("set2", 11))   # 从集合中删除指定值 11
print(r.smembers("set2"))