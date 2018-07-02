#author_by zhuxiaoliang
#2018-07-01 上午11:16
"""
测试python装饰器的执行顺序
经过和python_decorate_02,03文件的执行的结果
装饰器（未带参数的装饰器）的执行顺序是：
1、对于装饰器函数是从下往上开始执行，比如：
@f1
@f2
def f():
    pass
将按照f2—>f1->f的执行顺序执行
2、在执行到每个装饰器函数的内部函数，重点（内部函数）
先把装饰器内部函数之外的部分执行完毕，则进入内部函数执行
3、装饰器内部函数执行顺序按照从上往下的执行顺序，此处按照f1->f2->f的
顺序执行。
至于原因，没想出来，难道是栈？
2、装饰器带参数的执行顺序
第一层函数：从上倒下顺序
第二层函数：从下到下
第三层函数：从上倒下
具体原因没搞定
"""


import time
def outer1(*args):
    print(*args)
    def deco01(func):
        def wrapper(*args, **kwargs):
            print("this is deco01")
            #startTime = time.time()
            func(*args, **kwargs)
            #endTime = time.time()
            #msecs = (endTime - startTime)*1000
            #print("time is %d ms" %msecs)
            print("deco01 end here")
        return wrapper
    return deco01
def outer2(*args):
    print(*args)
    def deco02(func):
        def wrapper(*args, **kwargs):
            print("this is deco02")
            func(*args, **kwargs)

            print("deco02 end here")
        return wrapper
    return deco02

@outer1('outer1')
@outer2('outer2')
def func(a,b):
    print("hello，here is a func for add :")
    time.sleep(1)
    print("result is %d" %(a+b))
#f = deco01(deco02(func(3,4)))
func(3,4)

#if __name__ == '__main__':
#  f = func(3,1)
    #f(3,4)
"""
执行结果：
outer1
outer2
this is deco01
this is deco02
hello，here is a func for add :
result is 7
deco02 end here
deco01 end here

"""
