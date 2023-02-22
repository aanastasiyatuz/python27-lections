"=======================Словари======================="
# dict - изменяемый, итерируемый, неупорядоченный, неиндексируемый тип данных, предназначенный для хранения данных в парах (ключ:значение)

user = {
    'name':'Nastya',
    'age':13,
    'last_name':'Tuz'
}

print(user['name']) # 'Nastya'

# ключи в словаре будут уникальными, поэтому если в словарь добавить значение по уже существующему ключу, то сохранится последнее значение
dict1 = {'a':1, 'b':2, 'a':3, 'c':2}
# {'a':3, 'b':2, 'c':2}
a = 1
b = 2
a = 3
c = 2
# a=3 b=2 c=2

# ключами могут быть только хешируемые типы данных (неизменяемые типы данных)
print(hash(10)) # 10
print(hash('hello')) # 6344138726596412773
# print(hash([1,2,3]))  
# TypeError: unhashable type: 'list'
print(hash(  (1,2,3)  )) # 529344067295497451
# print(hash( (1,2,3,[]) ))
# TypeError: unhashable type: 'list'
dict1 = {
    105: 'some value',
    'key1': 'some val 2',
    (1,2,3): 'some val 3',
    None: 'some val 4',
    True: 'some val 5'
}
print(dict1[(1,2,3)]) # 'some val 3'
print(dict1[None]) # 'some val 4'

# dict2 = {
#     [1,2,3]:'hello'
# }
# TypeError: unhashable type: 'list'
dict2 = {
    'hello':[1,2,3]
}
dict2['hello'] # [1,2,3]

dict1 = {'a':1, 'b':2, 'c':3}
# dict1['d'] # KeyError: 'd'


"---------------------Создание---------------------"
dict1 = {'a':1, 'b':2, 'c':3}

dict2 = dict([('a', 1), ('b',2)])
# {'a':1, 'b':2}

list1 = ['a','b','c']
list2 = [1,2,3]
dict3 = dict(zip(list1, list2))
# {'a':1, 'b':2, 'c':3}

dict4 = {}
dict4['name'] = 'Nastya'
dict4['last_name'] = 'Tuz'
print(dict4) # {'name': 'Nastya', 'last_name': 'Tuz'}

"===================Методы словаря==================="
# get - метод, который принимает в себя ключ. Если такой ключ есть - возвращает его значение. Если такого ключа нет - возвращает None (или default значение)

user = {
    'name':'Nastya',
    'age':13,
    'last_name':'Tuz'
}

# user['id']   # KeyError: 'id'
user.get('id') # None
user.get('name') # 'Nastya'
user.get('id', 10) # 10
user.get('age', 20) # 13
# default (значение по умолчанию) - возвращается, если ключа нет. если есть ключ, возвращается его значение

# pop - метод, который принимает ключ, удалят пару под этим ключом. возвращает удаленное значение
dict1 = {'a':10, 'b':20, 'c':30}
res = dict1.pop('a')
print(dict1) # {'b':20, 'c':30}
print(res) # 10

# popitem - метод, который удаляет пару, которая была добавлена последней в словарь
dict1 = {'a':10, 'b':20, 'c':30}
res = dict1.popitem()
print(dict1) # {'a':10, 'b':20}
print(res) # ('c', 30)

# update - расширяет словарь вторым словарем
dict1 = {'a':1}
dict2 = {'b':2}
dict1.update(dict2)
print(dict1) # {'a':1, 'b':2}
print(dict2) # {'b':2}

"-----------------keys, values, items-----------------"
# keys - возвращает список ключей
# values - возвращает список значений
# items - возвращает список из пар (ключ, значение)

user = {
    'name':'Nastya',
    'age':13,
    'last_name':'Tuz'
}

print(user.keys())
# dict_keys(['name', 'age', 'last_name'])

print(user.values())
# dict_values(['Nastya', 13, 'Tuz'])

print(user.items())
# dict_items([('name', 'Nastya'), ('age', 13), ('last_name', 'Tuz')])

"================Итерирование слование================"
user = {
    'name':'Nastya',
    'age':13,
    'last_name':'Tuz'
}

for i in user: 
    # когда проходимся по словарю - получаем ключи
    print(i)
# 'name'  
# 'age'  
# 'last_name'

for i in user.keys():
    # когда итерируем dict_keys - проходимся по ключам
    print(i)
# 'name'  
# 'age'  
# 'last_name'

for i in user.values():
    # когда итерируем dict_values - проходимся по значениям
    print(i)
# 'Nastya'
# 13
# 'Tuz'

for i in user.items():
    # когда итерируем dict_items - проходимся по парам
    print(i)
# ('name','Nastya')
# ('age',13)
# ('last_name','Tuz')

for key, value in user.items():
    print(key) # 'name'
    print(value) # 'Nastya'

i = ('name','Nastya')
key, value = ('name','Nastya')

dict1 = {'a':1, 'b':2, 'c':3}
# создать новый словарь, где ключами будут значения из dict1, а значениями ключи из dict1
# res = {1:'a', 2:'b', 3:'c'}
res = {}
for key, value in dict1.items():
    res[value] = key
print(res)

res = dict(zip(dict1.values(), dict1.keys()))
print(res)

dict1 = {
    "a": {"aaa":1},
    "b": {"aaa":2},
    "c": {"aaa":3}
}
# res = {"a":1, "b":2, "c":3}
res = {}
for key, value in dict1.items():
    res[key] = value['aaa']
print(res)