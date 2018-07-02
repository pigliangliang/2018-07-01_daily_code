#author_by zhuxiaoliang
#2018-07-01 下午12:59

import time
import random


def timmer(func):
    def wrapper():
        start_time = time.time()
        func()
        stop_time = time.time()
        print('run time is %s' % (stop_time - start_time))

    return wrapper


def auth(func):
    def deco():
        name = input('name: ')
        password = input('password: ')
        if name == 'egon' and password == '123':
            print('login successful')
            func()  # wrapper()
        else:
            print('login err')

    return deco


@auth  # index = auth(timmer(index))
@timmer  # index = timmer(index)
def index():
    time.sleep(3)
    print('welecome to index page')


index()