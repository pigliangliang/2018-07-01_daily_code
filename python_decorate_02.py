#author_by zhuxiaoliang
#2018-07-01 上午11:25
def outera(*args):
    print(*args)
    def decorator_a(func):
        print('decorator_a')
        def inner_a(*args, **kwargs):
            #print('Get in decorator_a')
            print('Get in inner_a')
            return func(*args, **kwargs)

        return inner_a
    return decorator_a


def outerb(*args):
    print(*args)
    def decorator_b(func):
        print('decorator_b')
        def inner_b(*args, **kwargs):
            #print('Get in decorator_b')
            print('Get in inner_b')
            return func(*args, **kwargs)

        return inner_b
    return decorator_b

@outera("outera")
@outerb('outerb')
def f(x):
    print('Get in f')
    return x * 2


f(1)
"""
执行结果：
/Library/Frameworks/Python.framework/Versions/3.6/bin/python3.6 /Users/pig/PycharmProjects/2018-07-01/python_decorate_02.py
outera
outerb
decorator_b
decorator_a
Get in inner_a
Get in inner_b
Get in f
"""