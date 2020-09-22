mo1=__import__("des")
mo2=__import__("child.child")
mo3=__import__("child")

print(mo1,mo2,mo3)#mo3与mo2相同

#同级目录使用模块对象来调用
mo1.B()
mo1.fun2()

#对于目录下的，动态导入只会导入第一级目录
mo2.child.A()#虽然没有具体定义类体，但无错就是成功
mo2.child.fun1()
mo3.child.fun1()

