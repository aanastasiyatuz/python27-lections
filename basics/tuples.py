"=======================Кортеж======================="
# tuple - неизменяемый, итерируемый, индексируемый и упорядоченный тип данных, предназначенный для хранения элементов в строгом порядке. (в целом ничем не отличается от списков, просто неизменяемый, поэтому занимает меньше памяти)

tuple1 = (1,2,3,4)
tuple2 = (5) # int
tuple3 = 1,2,3,4 # tuple
tuple4 = 5, # tuple (5,)
tuple5 = (1,'hello', [2,3,4])
tuple5[-1].append(5)
# tuple5 = (1, 'hello', [2,3,4,5])
# tuple5[0] = 5 
# TypeError: 'tuple' object does not support item assignment
tuple6 = tuple('hello')
# ('h', 'e', 'l', 'l', 'o')

"====================Методы tuple===================="
# count - считает кол-во данного элемента в tuple
tuple1 = (1,2,1,4,1,5,1,6)
print(tuple1.count(1)) # 4
print(tuple1.count('hello')) # 0

# index - возвращает индекс данного элемента в tuple
tuple1 = ('hello', 'world', 105)
print(tuple1.index('hello')) # 0
print(tuple1.index('w')) # ValueError: tuple.index(x): x not in tuple
