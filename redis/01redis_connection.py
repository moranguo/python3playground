import redis   # 导入redis模块，通过python操作redis 也可以直接在redis主机的服务端操作缓存数据库

# 连接redis，加上decode_responses=True，写入的键值对中的value为str类型，不加这个参数写入的则为字节类型。
r = redis.Redis(host='localhost', port=6379, decode_responses=True)   # host是redis主机，需要redis服务端和客户端都启动 redis默认端口是6379
r.set('name', 'eric')  # key是"foo" value是"bar" 将键值对存入redis缓存
print(r['name'])
print(r.get('name'))  # 取出键name对应的值
print(type(r.get('name')))

r = redis.Redis(host='localhost', port=6379, decode_responses=False)   # host是redis主机，需要redis服务端和客户端都启动 redis默认端口是6379
r.set('name', 'eric')  # key是"foo" value是"bar" 将键值对存入redis缓存
print(r['name'])
print(r.get('name'))  # 取出键name对应的值
print(type(r.get('name')))

# result
# eric
# eric
# <class 'str'>
#
# b'eric'
# b'eric'
# <class 'bytes'>
