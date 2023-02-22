"=============================Exceptions============================="
# Исключения (ошибки) - обьекты, которые обрывают работу кода, если не были обработаны

SyntaxError
# исключение, которое выходит если допущена синтаксическая ошибка
""" 
(

SyntaxError: '(' was never closed
"""
# если используем ключевые слова не правильно
"""
break

SyntaxError: 'break' outside loop
"""
"""
if = 5

SyntaxError: invalid syntax
"""

TypeError
# исключение, которое выходит когда мы делаем что-то не свойственное данному типу данных
""" 
1 + '1'

TypeError: unsupported operand type(s) for +: 'int' and 'str'
"""

"""
for i in 123456789:
    ...
TypeError: 'int' object is not iterable
"""

# когда мы передаем в функцию больше или меньше аргументов, чем она требует
""" 
list1 = []
list1.pop(1,2,3,4)

TypeError: pop expected at most 1 argument, got 4
"""

"""  
list1 = []
list1.append()

TypeError: list.append() takes exactly one argument (0 given)
"""

KeyError
# когда мы обращаемся по несуществующему ключу
""" 
dict_ = {'a':1, 'b':2}
dict_['c']

KeyError: 'c' 
"""

""" 
dict_ = {'a':1, 'b':2}
dict_.pop('c')

KeyError: 'c' 
"""

NameError
# если нет такой переменной
""" 
print(djfrgbhkwhgr)

NameError: name 'djfrgbhkwhgr' is not defined 
"""

"""
a = 5
if a == 6:
    b = 7 # переменная создастся только если условие верное
print(b)

NameError: name 'b' is not defined 
"""

ValueError
# когда мы передаем в функцию то, что она не может корректно обработать
""" 
int('10a')

ValueError: invalid literal for int() with base 10: '10a' 
"""
# когда мы пытаемся распаковать не такое же кол-во элементов в несколько переменных

""" 
a,b = 1,2,3
a,b,c = 1,2
a,b = 1,2,3,4
ValueError: too many values to unpack (expected 2)
"""

AttributeError
# когда пытаемся обратиться к несуществующему методу в каком-то типе данных
""" 
list1 = []
list1.lower()
AttributeError: 'list' object has no attribute 'lower' 
"""

IndexError
# когда обращаяемся по несуществующему индексу
""" 
list1 = [1,2,3]
list1[100]
IndexError: list index out of range 
"""

""" 
list1 = []
list1.pop()
IndexError: pop from empty list
"""

ModuleNotFoundError
# когда пытаемся обратится к несуществующей библеотеки
""" 
import django
ModuleNotFoundError: No module named 'django'
"""

ZeroDivisionError
# когда делим на 0
""" 
10 / 0
ZeroDivisionError: division by zero
"""

IndentationError
# когда мы не соблюдаем отступы
""" 
 v = 10

IndentationError: unexpected indent 
"""

""" 
if True:
print("hello")

IndentationError: expected an indented block after 'if' statement on line 132 
"""

Exception
# исключение, которое создали чтобы его вызывать

# чтобы вызвать исключение, используем raise
# raise Exception('Hello')


"========================Обработка исключений========================"
# чтобы наш код не ломался, мы можем использовать конструкцию try-except и обраюотать исключение

try:
    # код, который возможно вызовет ошибку
    num = int(input("Введите число: "))
except TypeError:
    # код, который отработает только если в блоке try вызвалась ошибка ValueError
    print("Вы ввели не число")
else:
    # код, который отработает только если в блоке try ни одна ошибка не вызвалась
    print("Введенное число", num)
finally:
    # код, который отрабатывает вообще в любом случае
    # хоть вызвалась ошибка, хоть не вызвалась
    print("До свидания")

# минимальная конструкция состоит из try-except или try-finally
# можно использовать несколько except
try:
    num1 = int(input("Введите 1 число "))
    num2 = int(input("Введите 2 число "))
    print(num1 // num2)
except ValueError:
    print('Вы ввели не число')
except ZeroDivisionError:
    print("Нельзя делить на 0")

try:
    num1 = int(input("Введите 1 число "))
    num2 = int(input("Введите 2 число "))
    print(num1 // num2)
except (ValueError, ZeroDivisionError):
    print('Введены не корректные данные')

# можно отловить любые исключения используя просто except
try:
    raise NameError
except:
    print("Любая ошибка")

# можно отловить любые ошибки отлавливая Exception
try:
    int('12d')
except Exception as e:
    print(type(e))

# try:
#     print(1+'1') # TypeError
# except TypeError:
#     try:
#         print(int('10a')) # ValueError
#         print("первый except")
#     except ValueError:
#         print("вложенный except")
# except ValueError:
#     print("второй except")
# finally:
#     print("все")
