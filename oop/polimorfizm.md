# Полиморфизм
> принцип ООП, в котором методы в разных классах называются одинаково. (один интерфейс - разная реализация)

```py
class Dog:
    def speak(self):
        print("гав-гав")

class Cat:
    def speak(self):
        print("мяу-мяу")

class Frog:
    def speak(self):
        print("ква-ква")

animals = [Cat(), Frog(), Dog(), Cat(), Dog(), Frog()]
for animal in animals:
    animal.speak()
```