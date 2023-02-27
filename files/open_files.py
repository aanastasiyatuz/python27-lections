"===================Пакеты и модули==================="
# module - любой файл с расширением .py

# import test
# print(test.a)

# from test import a
# print(a)

# package - набор модулей (в папке обязательно должен быть __init__.py)

# from package.test1 import hello
# from package.test2 import list1


"==================Работа с файлами=================="
# open - функция, которая позволяет открывать файлы в определенном режиме
# r - read (только для чтения)
# w - write (только для перезаписи, каждый раз при открытии очищает файл)
# a - append (только для дозаписи, добавляется в конец)
# x - сойдает файл, но если файл уже есть - ошибка
# b - бинарный вид

"========================Read========================"
file = open('test.txt', 'r')
# если такого файла нет - выйдет ошибка
# если не указать режим - откроется в режиме чтения

print(dir(file))

print("readable", file.readable()) # True
print("writable", file.writable()) # False

print(file.read()) # считывает от начала до конца
print(file.read()) # '', потому что каретка в коце файла
file.seek(0) # перенос каретки в начало (на индекс 0)
print(file.read()) # считывает от начала до конца

file.seek(5)
print(file.read()) # считываем от 5 индекса до конца

file.seek(0)
print(file.read(5)) # 'Hello' считываем 5 символов
print(file.read()) # '\nWorld\nMakers\n' считваем от 5 до конца

file.seek(0)
print(file.readline()) # 'Hello\n' считывает до \n
print(file.readline()) # 'World\n' считывает до \n

file.seek(0)
print(file.readlines())
# ['Hello\n', 'World\n', 'Makers\n']

file.seek(10)
print(file.tell()) # 10

file.read() # считал до конца (на 19 индекс)
print(file.tell()) # 19

# file.write("hello")
# io.UnsupportedOperation: not writable
# !запись в режиме чтения запрещена

print(file.name) # 'test.txt'
print(file.closed) # False
file.close() # !важно закрывать файлы
print(file.closed) # True


"========================Write========================"
file = open("new_file.txt", 'w')
# если файл нет - создает
# если есть - очищает

print("readable", file.readable()) # False
print("writable", file.writable()) # True

# file.read()
# io.UnsupportedOperation: not readable
# !в режиме записи чтение запрещено

file.write('Hello ')
file.write('Makers')
# Hello Makers

file.writelines(['Hello', 'World'])
# Hello MakersHelloWorld

file.writelines(['\nNew\nLine'])
# Hello MakersHelloWorld
# New
# Line

file.seek(0)
file.write("AAA")
# AAAlo MakersHelloWorld
# New
# Line

file.close()

"=======================Append======================="
file = open("new_file2.txt", 'a')
# если файла нет - создается новый

print("readable", file.readable()) # False
print("writable", file.writable()) # True

file.write('Hello')
# дозапись идет в конец файла (старые данные не удаляются)

file.seek(0)
file.write("New")
# все равно в конец дозапись

file.close()


"================Контекстный менеджер================"

# try:
#     file = open("aaa.txt", 'w')
#     file.read()
# finally:
#     file.close()


with open('test.txt') as f:
    f.read()
    f.seek(0)
    f.read()
    print(f.closed) # False
# файл закрывается   
print(f.closed) # True

with open("python.jpg", 'rb') as image:
    print(image.read())

with open("python.jpg", 'rb') as image:
    binary_image = image.read()

with open("new_image.jpg", 'wb') as file:
    file.write(binary_image)
