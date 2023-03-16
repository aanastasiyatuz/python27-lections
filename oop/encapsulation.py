class A:
    attr1 = 'public'
    _attr2 = 'protected'
    __attr3 = 'private'

print(A.attr1)
print(A._attr2)
# print(A.__attr3)
print(A._A__attr3)
print(dir(A))

class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age
    
    def get_age(self):
        return self.__age
    
    def set_age(self, new_age):
        if new_age > 0 and new_age < 120:
            self.__age = new_age
        else:
            raise Exception("Invalid age")

obj = Person('Nastya', 12)
print(obj.name)
print(obj.get_age())
obj.set_age(45)
print(obj.get_age())
# obj.set_age(125) Exception



class A:
    @property
    def hello(self):
        return 5

    # property.setter работает когда мы пишем obj.attr = ... 
    @hello.setter
    def hello(self, new_value):
        print("setter")

    # property.deleter работает когда мы пишем del obj.attr
    @hello.deleter
    def hello(self):
        print("deleter")

obj = A()
print(obj.hello)
obj.hello = 'new value'
del obj.hello


class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age
    
    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, new_age):
        if new_age > 0 and new_age < 120:
            self.__age = new_age
        else:
            raise Exception("Invalid age")
    
    @age.deleter
    def age(self):
        if self.__age < 100:
            raise Exception("Cannot delete age")
        del self.__age

obj = Person('Nastya', 12)
print(obj.age)
obj.age = 34
print(obj.age)
# obj.age = -100  # Exception: Invalid age
# del obj.age  # Exception: Cannot delete age
obj.age = 115
del obj.age
