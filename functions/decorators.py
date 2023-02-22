"======================Декоратор======================"
# декоратор - функция высшего порядка, которая нужна чтобы расширять функционал другой функции, не меняя ее

def decorator(func):
    def wrapper():
        print("Функция вызывается")
        func()
        print("Функция завершила работу")
    return wrapper

def func():
    print('hello')

res = decorator(func)
print(res)
# <function decorator.<locals>.wrapper at 0x7fd023b12200>
res()
# Функция вызывается
# hello
# Функция завершила работу

func()
# hello


"================Синтаксический сахар================"
def decorator(func):
    def wrapper():
        print("Функция вызывается")
        func()
        print("Функция завершила работу")
    return wrapper

@decorator    # func = decorator(func)
def func():
    print('hello')

func()
# Функция вызывается
# hello
# Функция завершила работу

print(func)
# <function decorator.<locals>.wrapper at 0x7f1e36656440>

# @decorator
def func(string):
    print(string)

func("Hello")
# TypeError: decorator.<locals>.wrapper() takes 0 positional arguments but 1 was given


def decorator(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
    return wrapper


def func(a,b):
    print(a, b)

func(4,6)
func(a=5,b=3)
func(b=5,a=3)

dict_ = {'a':10, 'b':15}
func(**dict_)

tuple_ = (34, 54)
func(*tuple_)

from datetime import datetime

def timer(func):
    def wrapper(*args, **kwargs):
        start = datetime.now()
        res = func(*args, **kwargs)
        end = datetime.now()
        print(f"Функция отработала за {end-start}")
        return res
    return wrapper

from functools import cache
@timer
@cache
def func(count):
    return sum(range(count))

print(func(count=100000000))
print(func(count=100000000))

@timer
def func(a,b):
    print(a,b)

func(1,4)


# <b>text</b> - жирный
# <i>text</i> - курсив

def bold(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        return f'<b>{res}</b>'
    return wrapper

def italic(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        return f'<i>{res}</i>'
    return wrapper

@bold
@italic
def func(string):
    return f'Hello {string}'
# func = bold(italic(func))

print(func('Makers'))


def func(count):
    return sum(range(count))

start = datetime.now()
func(100)
end = datetime.now()
print(end-start)

start = datetime.now()
func(500)
end = datetime.now()
print(end-start)
