class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        pass

class Mammal(Animal):
    def __init__(self, name, hair_color):
        super().__init__(name)
        self.hair_color = hair_color

    def sound(self):
        return "Mammal sound"

class Dog(Mammal):
    def __init__(self, name, hair_color, breed):
        super().__init__(name, hair_color)
        self.breed = breed

    def sound(self):
        return "Dog sound"

class Cat(Mammal):
    def __init__(self, name, hair_color, color):
        super().__init__(name, hair_color)
        self.color = color

    def sound(self):
        return "Cat sound"

dog = Dog("Bulldog", "qora", "bulldog")
cat = Cat("Siam", "sarg'ona", "siam")

print(dog.sound())  # Dog sound
print(cat.sound())  # Cat sound
print(dog.name)     # Bulldog
print(dog.hair_color) # qora
print(dog.breed)     # bulldog
print(cat.name)      # Siam
print(cat.hair_color) # sarg'ona
print(cat.color)     # siam
```

Multilevel inheritance: 
```python
class Animal:
    def __init__(self, name):
        self.name = name

class Mammal(Animal):
    def __init__(self, name, hair_color):
        super().__init__(name)
        self.hair_color = hair_color

class Dog(Mammal):
    def __init__(self, name, hair_color, breed):
        super().__init__(name, hair_color)
        self.breed = breed
