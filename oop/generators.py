gen = (x for x in range(10))
print(gen)
# <generator object <genexpr> at 0x7f16570d2420>

def generator(n):
    for i in range(1, n+1):
        yield i**2

print(generator(10))
# <generator object generator at 0x7ff7bc65e490>

gen = generator(10)
print(next(gen)) # 1
print(next(gen)) # 4
print(next(gen)) # 9
print(list(gen)) # [16, 25, 36, 49, 64, 81, 100]

for i in generator(5):
    print(i)
# 1
# 4
# 9
# 16
# 25

gen = generator(15)
while True:
    try:
        print(next(gen))
    except StopIteration:
        break
# 1 4 9 16 25 36 49 64 81 100 121 144 169 196 225

class IterInt(int):
    def __iter__(self):
        for i in str(self):
            yield int(i)

    def __len__(self):
        return len([i for i in self])

    def __getitem__(self, index):
        return [i for i in self][index]


a = IterInt(1234567)

for i in a:
    print(i)

print(8 in a)
print(5 in a)
print(len(a))
print(a[-1])
print(a[1:4])

print(a+1)



string1 = 'abcefghjkl'
string2 = 'gfdjh'
print(string1 > string2)



class MyStr:
    def __init__(self, string):
        self.string = string
    
    def __len__(self):
        return len(self.string)
    
    def __eq__(self, other):
        return len(self) == len(other)

    def __ge__(self, other):
        return len(self) >= len(other)

    def __le__(self, other):
        return len(self) <= len(other)

    def __gt__(self, other):
        return len(self) > len(other)

    def __lt__(self, other):
        return len(self) < len(other)

    def __ne__(self, other):
        return len(self) != len(other)


string_obj_1 = MyStr('hello')
string_obj_2 = MyStr('abcde')
print(len(string_obj_1))
print(string_obj_1 == string_obj_2)

# __eq__ ==
# __ge__ >=
# __gt__ >
# __le__ <=
# __lt__ <
# __ne__ !=


class A:
    attr1 = 'aaa'

    def __getattribute__(self, name):
        print("__getattribute__", name)
        return super().__getattribute__(name)
    
    def __setattr__(self, name, value):
        print("__setattr__", name, value)
        return super().__setattr__(name, value)
    
    def __delattr__(self, name):
        print("__delattr__", name)
        return super().__delattr__(name)

obj = A()
obj.attr1 # obj.__getattribute__('attr1')
obj.attr1 = 'bbbb' # obj.__setattr__('attr1', 'bbbb')
del obj.attr1

print(A.__dict__) # {'attr1': 'aaa'}
obj = A()
print(obj.__dict__) # {}
obj.attr1 = 'bbb'
print(obj.__dict__) # {'attr1': 'bbb'}
del obj.attr1
print(obj.__dict__) # {}
print(obj.attr1) # 'aaa'


getattr(obj, 'attr1') # obj.attr1
setattr(obj, 'new_attr', 'ccc') # obj.new_attr = 'ccc' 
delattr(obj, 'new_attr') # del obj.new_attr
hasattr(obj, 'dsfgh') # True/False 
