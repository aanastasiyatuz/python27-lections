"=====================Функции====================="
# функция - именованный блок кода, который принимает аргументы и возвращает результат

my_sum = lambda num1, num2: num1 + num2
res = my_sum(5, 10)
print(res) # 15
print(my_sum) # <function <lambda> at 0x7f70284f7d30>
# lambda - ключевое слово, для создания анонимной функции

def my_sum2(num1, num2):
    return num1 + num2
print(my_sum2) # <function my_sum2 at 0x7f1f1cca9040>
res = my_sum2(13, 45)
print(res) # 58

def calc(num1, num2, oper):
    """
    oper - строка, с операцией для вычислений
    "+" - сложение
    "-" - вычитание
    """

    if oper == '+':
        return num1 + num2
    if oper == '-':
        return num1 - num2
    if oper == '*':
        return num1 * num2
    if oper == '/':
        return num1 / num2

print(calc(10, 12, '+')) # 22
print(calc(20, 8, '-')) # 12
print(calc(10, 2, '*')) # 20
print(calc(15, 5, '/')) # 3.0
print(calc(15, 23, '5')) # None

def my_len(obj):
    "Возвращает длину обьекта"
    count = 0
    for i in obj:
        count += 1
        # count = count + 1
    return count

print(my_len([15,23,64,23,12])) # 5
print(my_len('abdjtrekg')) # 9
print(my_len({'a':1,'b':2})) # 2

def super_len(obj):
    try:
        # если мы можем итерировать обьект
        return my_len(obj)
    except TypeError:
        # если не можем, то будем итерировать его в виде строки
        return my_len(str(obj))

print(super_len([1,2,3,4])) # 4
print(super_len(123456789)) # 9 ('123456789')
print(super_len(None)) # 4 ('None')

"=======================DRY======================="
# DRY - don't repeat yourself (не повторяйся)

# представим, что у нас нет функции len

str_ = "Hello world"
count = 0
for i in str_:
    count += 1
# count - длина строки str_

list_ = [1,2,3,4,4,56,5,7,8]
count = 0
for i in list_:
    count += 1
# count - длина списка list_

def len_(obj):
    count = 0
    for i in obj:
        count += 1
    return count

str_ = 'Hello world'
count = len_(str_)

list_ = [1,2,3,4,4,56,5,7,8]
count = len_(list_)

"==============Аргументы и параметры=============="
# параметры - локальные переменные, значения которым мы задаем при вызове функции
# аргументы - значения, которые мы задаем параметрам при вызове функции
def func(parameter):
    local_var = 5
    print(locals())
    # {'parameter': 6, 'local_var': 5}

func(6)
# print(local_var) NameError
# print(parameter) NameError

"==========Виды параметров=========="
# 1. обязательные
# 2. необязательные
# 2.1 с дефолтным значением (по умолчанию)
# 2.2 args (arguments)
# 2.3 kwargs (key word arguments)

def func(a, b='default', *args, **kwargs):
    # args - tuple, куда попадут все позиционные аргументы, которые не попали по позиции
    # kwargs - dict, куда попадут все именованные аргументы, которые не попали по имени
    print(a, b, args, kwargs)

# func()
# TypeError: func() missing 1 required positional argument: 'a'
func('hello') # 'hello' 'default' () {}
func('hello', 100) # 'hello' 100 () {}
func('hello', 100, 84, 23, 'world')
# 'hello' 100 (84, 23, 'world') {}
func('hello', 100, 10, 20, 30, key1='value1', key2=500)
# 'hello' 100 (10, 20, 30) {'key1': 'value1', 'key2': 500}

# func('hello', a=100)
# TypeError: func() got multiple values for argument 'a'

"=================Виды аргументов================="
# позиционные (по порядку параметров)
# именнованные (по имени параметров)

def func2(a, b):
    print(f"a={a}, b={b}")

func2(10, 20) # позиционно
# a=10, b=20

func2(a=30, b=40) # именованно
# a=30, b=40

func2(b=50, a=60)
# a=60, b=50

"====================Звездочки===================="
list1 = [1,2,3,4]
list2 = [*list1]
# list2 = [1,2,3,4]

dict1 = {'a':1, 'b':2}
list3 = [*dict1]
# list3 = ['a', 'b']
dict2 = {**dict1}
# dict2 = {'a':1, 'b':2}
