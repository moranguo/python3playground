import redis
# pip instal redis

def script_load(script):
    sha = [None]
    def call(conn, keys=[], args=[], force_level=False):
        if not force_level:
            if not sha[0]:
                sha[0] = conn.execute_command(
                    "SCRIPT","LOAD", script, parse="LOAD"
                )
                print("script sha1 is %s" % sha[0])
                try:
                    return conn.execute_command(
                        # EVALSHA sha1 numkeys key [key ...] arg [arg ...]
                        "EVALSHA", sha[0], len(keys), *(keys+args)
                    )
                except redis.exceptions.ResponseError as msg:
                    if not msg.args[0].startwith("NOSCRIPT"):
                        raise
        return conn.execute_command(
            # EVAL script numkeys key [key ...] arg [arg ...]
            "EVAL", script, len(keys), *(keys+args)
        )
    return call

conn = redis.Redis()
# method 1, use our custom script_load function
# redis.sha1hex can get the sha1 of lua script
# the print in lua script, will print the log in redis_server 
lua_script_string = '''
    local sha1 = redis.sha1hex(ARGV[1])
    print(sha1)
    redis.call('set', 'hello','world')
    return {"set key hello with value world", sha1}
    '''
ret1 = script_load(lua_script_string)
print(ret1(conn,args=[lua_script_string]))

#method 2, use register_script
lua_script_string2 = '''
    local value = redis.call('get', 'hello')
    return {value, KEYS[1], KEYS[2], ARGV[1], ARGV[2], ARGV[3]}
    '''
ret2 = conn.register_script(lua_script_string2)
print(ret2(keys=["key1","key2"],args=["arg1","arg2","arg3"]))

# check lua script is load in cache
# SCRIPT EXISTS sha1

# result
# D:\eric_huang\software\Redis-x64-3.2.100>python loadlua.py
# script sha1 is b'4fb685bf8e376a69992a10cb5d58f41c3969f007'
# [b'set key hello with value world', b'4fb685bf8e376a69992a10cb5d58f41c3969f007']
# [b'world', b'key1', b'key2', b'arg1', b'arg2', b'arg3']