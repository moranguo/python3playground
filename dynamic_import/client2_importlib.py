import importlib
mo1= importlib.import_module('des')
mo2= importlib.import_module('child.child')
print(mo1,mo2)#mo2直接到child.child

des_B= mo1.B()
mo1.fun2()

mo2.fun1()


''' 
importlib使用场景
    1.动态切换模块
    2.使用反射判断是否有对应类、方法，无则设置
'''
mo3= importlib.import_module('child')
def func4():
    print(" run in func4")

print('mo3 all attr is ', dir(mo3))
print('mo3 has child is ', hasattr(mo3, "child")) # True
print('mo3.child all attr is ', dir(mo3.child))

if hasattr(mo3,"child1"):
    print("yes")
    c=getattr(mo3,"child")
else: #没有则设置
    setattr(mo3,"func4",func4)

mo3.func4()