import redis

# 可以直接建立一个连接池，然后作为参数Redis，这样就可以实现多个Redis实例共享一个连接池
pool = redis.ConnectionPool(host='localhost', port=6379, decode_responses=True)
r = redis.Redis(connection_pool=pool)

# clear all data in redis
r.flushdb()

# 默认的情况下，管道里执行的命令可以保证执行的原子性，执行pipe = r.pipeline(transaction=False)可以禁用这一特性。
# pipe = r.pipeline(transaction=False)
# pipe = r.pipeline(transaction=True)
pipe = r.pipeline()

# pipe.set('name', 'jack')
# pipe.set('role', 'operation')
# pipe.sadd('faz', 'baz')
# pipe.incr('num') # 如果num不存在则vaule为1，如果存在，则value自增1
# pipe.execute()

# 管道的命令可以写在一起
pipe.set('name', 'jack').set('role', 'operation').sadd('faz','baz').incr('num').execute()

print(r.get('name'))
print(r.get('role'))
print(r.get('num'))
