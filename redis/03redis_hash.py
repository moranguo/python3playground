import redis
import time

pool = redis.ConnectionPool(host='localhost', port=6379, decode_responses=True)
r = redis.Redis(connection_pool=pool)

r.hset("hash1", "k1", "v1")
r.hset("hash1", "k2", "v2")
print(r.hkeys("hash1")) # 取hash中所有的key
print(r.hget("hash1", "k1"))    # 单个取hash的key对应的值
print(r.hmget("hash1", "k1", "k2")) # 多个取hash的key对应的值
r.hsetnx("hash1", "k2", "v3") # 只能新建
print(r.hget("hash1", "k2"))

r.hmset("hash2", {"k2": "v2", "k3": "v3"})
print(r.hget("hash2", "k2"))  # 单个取出"hash2"的key-k2对应的value
print(r.hmget("hash2", "k2", "k3"))  # 批量取出"hash2"的key-k2 k3对应的value --方式1
print(r.hmget("hash2", ["k2", "k3"]))  # 批量取出"hash2"的key-k2 k3对应的value --方式2

print(r.hgetall("hash1"))
print(r.hlen("hash1"))

print(r.hkeys("hash1"))
print(r.hvals("hash1"))

print(r.hexists("hash1", "k4"))  # False 不存在
print(r.hexists("hash1", "k1"))  # True 存在

print(r.hgetall("hash1"))
r.hset("hash1", "k2", "v222")   # 修改已有的key k2
r.hset("hash1", "k11", "v1")   # 新增键值对 k11
r.hset("hash1", "k12", "v2")   # 新增键值对 k12
r.hdel("hash1", "k12")    # 删除一个键值对
print(r.hgetall("hash1"))

r.hset("hash1", "k3", 123)
r.hincrby("hash1", "k3", amount=-1)
print(r.hgetall("hash1"))
r.hincrby("hash1", "k4", amount=1)  # 不存在的话，value默认就是1
print(r.hgetall("hash1"))

r.hset("hash1", "k5", "1.0")
r.hincrbyfloat("hash1", "k5", amount=-1.0)    # 已经存在，递减-1.0
print(r.hgetall("hash1"))
r.hincrbyfloat("hash1", "k6", amount=-1.0)    # 不存在，value初始值是-1.0 每次递减1.0
print(r.hgetall("hash1"))

# 分片读取
# hscan(name, cursor=0, match=None, count=None)
# 增量式迭代获取，对于数据大的数据非常有用，hscan可以实现分片的获取数据，并非一次性将数据全部获取完，从而防止内存被撑爆
# 参数：
# name，redis的name
# cursor，游标（基于游标分批取获取数据）
# match，匹配指定key，默认None 表示所有的key
# count，每次分片最少获取个数，默认None表示采用Redis的默认分片个数
# 如：
# 第一次：cursor1, data1 = r.hscan('xx', cursor=0, match=None, count=None)
# 第二次：cursor2, data1 = r.hscan('xx', cursor=cursor1, match=None, count=None)
# ...
# 直到返回值cursor的值为0时，表示数据已经通过分片获取完毕
for i in range(1023):
    r.hset('hash3','k'+str(i), 'v'+str(i))
cursor1, data1 = r.hscan("hash3",count=10)
print(cursor1, data1)
print(r.hscan("hash3",cursor=cursor1,count=10))

# Make an iterator using the HSCAN command so that the client doesn't need to remember the cursor position.
# hscan_iter(name, match=None, count=None)
# 利用yield封装hscan创建生成器，实现分批去redis中获取数据
# 参数：
# match，匹配指定key，默认None 表示所有的key
# count，每次分片最少获取个数，默认None表示采用Redis的默认分片个数
# 如：
for i in range(1023):
    r.hset('hash4','k'+str(i), 'v'+str(i))
for item in r.hscan_iter('hash4', count=100):
    print(item)
print(r.hscan_iter("hash4"))    # 生成器内存地址
