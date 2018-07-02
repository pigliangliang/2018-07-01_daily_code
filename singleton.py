#author_by zhuxiaoliang
#2018-07-01 上午10:54
#单例模式的实现方式
"""
一、使用模块实现
其实，Python 的模块就是天然的单例模式，因为模块在第一次导入时，会生成 .pyc 文件，
当第二次导入时，就会直接加载 .pyc 文件，而不会再次执行模块代码。
"""
class Singleton(object):
    def foo(self):
        pass

singleton = Singleton()#使用时直接导入singleton对象即可。

"""
二、装饰器实现
"""
def decorator(cls):
    _instance ={}

    def inner(*args,**kwargs):

        if cls not in _instance:
            _instance[cls]=cls(*args,**kwargs)
        return _instance
    return inner

@decorator
class A(object):

    def __init__(self):
        pass

a1 = A()
a2 = A()
print(a1,a2)

print(id(a1))
print(id(a2))
"""
执行结果：

{<class '__main__.A'>: <__main__.A object at 0x1014605f8>} {<class '__main__.A'>: <__main__.A object at 0x1014605f8>}
4303190920
4303190920
"""

#三、使用类方式

class Singleton(object):
    def __init__(self):
        pass

    @classmethod
    def instance(cls,*args,**kwargs):

        if not hasattr(Singleton,'_instance'):
            Singleton._instance =Singleton(*args,**kwargs)
        return  Singleton._instance

print(id(Singleton.instance()),id(Singleton.instance()))
#输出相同：4316224424 4316224424
