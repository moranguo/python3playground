import redis
import time

pool = redis.ConnectionPool(host='localhost', port=6379, decode_responses=True)
r = redis.Redis(connection_pool=pool)

r.zadd("zset1", {'n1': 11, 'n2': 22})
r.zadd("zset2", {'m1': 22, 'm2': 44})
print(r.zcard("zset1")) # 集合长度
print(r.zcard("zset2")) # 集合长度
print(r.zrange("zset1", 0, -1))   # 获取有序集合中所有元素
print(r.zrange("zset2", 0, -1, withscores=True))   # 获取有序集合中所有元素和分数

print(r.zrevrange("zset1", 0, -1))    # 只获取元素，不显示分数
print(r.zrevrange("zset1", 0, -1, withscores=True)) # 获取有序集合中所有元素和分数,分数倒序

for i in range(1, 30):
   element = 'n' + str(i)
   r.zadd("zset3", {element:i})
print(r.zrangebyscore("zset3", 15, 25)) # # 在分数是15-25之间，取出符合条件的元素
print(r.zrangebyscore("zset3", 12, 22, withscores=True))    # 在分数是12-22之间，取出符合条件的元素（带分数）

print(r.zrevrangebyscore("zset3", 22, 11, withscores=True)) # 在分数是22-11之间，取出符合条件的元素 按照分数倒序

print(r.zscan("zset3"))

# for i in r.zscan_iter("zset3"): # 遍历迭代器
#     print(i)

print(r.zrange("zset3", 0, -1, withscores=True))
print(r.zcount("zset3", 11, 22))

r.zincrby("zset3", 2, "n2")    # 每次将n2的分数自增2
print(r.zrange("zset3", 0, -1, withscores=True))

print(r.zrank("zset3", "n1"))   # n1的索引号是0 这里按照分数顺序（从小到大）
print(r.zrank("zset3", "n6"))   # n6的索引号是5

print(r.zrevrank("zset3", "n1"))    # n1的索引号是29 这里安照分数倒序（从大到小）

r.zrem("zset3", "n3")   # 删除有序集合中的元素n3 删除单个
print(r.zrange("zset3", 0, -1))

r.zremrangebyrank("zset3", 0, 1)  # 删除有序集合中的索引号是0, 1的元素
print(r.zrange("zset3", 0, -1))

r.zremrangebyscore("zset3", 11, 22)   # 删除有序集合中的分数是11-22的元素
print(r.zrange("zset3", 0, -1))

print(r.zscore("zset3", "n27"))   # 获取元素n27对应的分数27

