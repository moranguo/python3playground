# 51.打乱一个排好序的list对象alist？
import random
alist = [1,2,3,4,5]
random.shuffle(alist)
print(alist)

# 下面这段代码是shuffle的实现
# items = list(alist)
# for i in xrange(len(alist)):
#     alist[i] = items.pop(self.randrange(len(items)))