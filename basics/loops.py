"========================Циклы========================"
# цикл - блок кода, который отрабатывается несколько раз
# for - цикл, который работает с итерируемыми обьектами, цикл заканчивает свою работу, когда он доходит до последнего элемента в итерируемом обьекте
# while - цикл, который работает до тех пор, пока условие верное

list1 = ['hello', 10, True, [1,2,3]]
for element in list1:
    print(element)

string1 = 'hello world'
for letter in string1:
    print(letter)

i = 1
while i != 10:
    print("hello", i)
    i = i + 1

i = 0
while i: # вообще ни разу не отработает, потому что 0 это False
    print("hello world")
    i = i + 1


"===============Ключевые слова в циклах==============="
# break - полностью останавливает цикл
# continue - переход к следующей итерации

for i in range(10):
    if i == 3:
        break
    print(i)
# 0
# 1
# 2

for i in range(10):
    if i == 3:
        continue
    print(i)
# 0 1 2 4 5 6 7 8 9

for i in range(10):
    print(i)
    break
# 0

for i in range(10):
    print(i)
    continue
# 0 1 2 3 4 5 6 7 8 9


list1 = [1,2,3,1,2,4,5,9,1,1,5,7,7]
# с помощью метода remove удалите все единицы в списке
while 1 in list1:
    list1.remove(1)
print(list1)
