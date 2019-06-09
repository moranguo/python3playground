import redis
import time


pool = redis.ConnectionPool(host='localhost', port=6379, decode_responses=True)
r = redis.Redis(connection_pool=pool)
# clear all data in redis
r.flushdb()

# String
# set(name, value, ex=None, px=None, nx=False, xx=False)

# ex，过期时间（秒） 这里过期时间是3秒，3秒后p，键food的值就变成None
r.set('food', 'mutton', ex=3)
print(r.get('food'))
print("sleep for 3 seconds")
time.sleep(3)
print(r.get('food'))

# px，过期时间（豪秒） 这里过期时间是3豪秒，3毫秒后，键foo的值就变成None
r.set('food', 'beef', px=3)
print(r.get('food'))

# nx，如果设置为True，则只有name不存在时，当前set操作才执行 （新建）
print(r.set('fruit', 'watermelon', nx=True))    # True--不存在
# 如果键fruit不存在，那么输出是True；如果键fruit已经存在，输出是None

# xx，如果设置为True，则只有name存在时，当前set操作才执行 （修改）
print((r.set('fruit', 'watermelon1', xx=True)))   # True--已经存在
# 如果键fruit已经存在，那么输出是True；如果键fruit不存在，输出是None

print(r.setnx('fruit1', 'banana'))  # fruit1不存在，输出为True

# setex key seconds value
r.setex("fruit2", 5, "orange")
print(r.get('fruit2'))

# psetex(name, time_ms, value)
r.psetex("fruit3", 5000, "apple")
time.sleep(5)
print(r.get('fruit3'))  # 5000毫秒后，取值就从apple变成None

r.mset({'k1': 'v1', 'k2': 'v2'})
print(r.mget("k1", "k2"))
print(r.mget(['k1', 'k2']))
print(r.mget("k1"))

r.set('food', 'beef')
print("old value is %s " % r.getset("food", "barbecue"))  # 设置的新值是barbecue 设置前的值是beef
print("new value is %s " % r.get('food'))

r.set("cn_name", "中国崛起") # 汉字
print(r.getrange("cn_name", 0, 2))   # 取索引号是0-2 前3位的字节 中 切片操作 （一个汉字3个字节 1个字母一个字节 每个字节8bit）
print(r.getrange("cn_name", 0, -1))  # 取所有的字节 中国崛起 切片操作
r.set("en_name","erichuang") # 字母
print(r.getrange("en_name", 0, 2))  # 取索引号是0-2 前3位的字节 eri 切片操作 （一个汉字3个字节 1个字母一个字节 每个字节8bit）
print(r.getrange("en_name", 0, -1)) # 取所有的字节 erichuang 切片操作

# setrange key offset value
# 修改字符串内容，从指定字符串索引开始向后替换（新值太长时，则向后添加)
r.setrange("en_name", 1, "ccc")
print(r.get("en_name"))


r.set('n1', 'foo')
print(r.get('n1'))
# 01100110 01101111 01101111
for i in r.get('n1'):
    num = ord(i)
    print(bin(num).replace('b',''), end=' ')
r.setbit('n1', 7, 1)
print('\n')
print(r.get('n1'))
# 01100111 01101111 01101111
for i in r.get('n1'):
    num = ord(i)
    print(bin(num).replace('b',''), end=' ')
print('\n')


print(r.getbit("n1", 6)) # 1
print(r.getbit("n1", 7)) # 1

print(r.bitcount("n1",0,1))  # 11 表示前2个字节中，1出现的个数

# bitop("AND", 'new_name', 'n1', 'n2', 'n3')
# 获取Redis中n1,n2,n3对应的值，然后将所有的值做位运算（求并集），然后将结果保存 new_name 对应的值中
r.set("foo","1")  # 0000001
r.set("foo1","2")  # 0000010
print(r.mget("foo","foo1"))
print(r.bitop("AND","new","foo","foo1"))  # "new" 0 0000000
print(r.mget("foo","foo1","new"))

r.set('foo', 'goo1')
print(r.strlen("foo"))  # 4 'goo1'的长度是4

r.set("visit:12306:totals", 34634)
print(r.get("visit:12306:totals"))
r.incr("visit:12306:totals")
r.incr("visit:12306:totals")
print(r.get("visit:12306:totals"))

r.set("foo1", "123.0")
r.set("foo2", "221.0")
print(r.mget("foo1", "foo2"))
r.incrbyfloat("foo1", amount=2.0)
r.incrbyfloat("foo2", amount=3.0)
print(r.mget("foo1", "foo2"))

r.set("foo1", 5)
r.set("foo4", 5)
r.decr("foo4", amount=3) # 递减3
r.decr("foo1", amount=1) # 递减1
print(r.mget("foo1", "foo4"))

r.set('name', 'eric')
r.append("name", "huang")
print(r.mget("name"))

