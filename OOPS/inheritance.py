class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

# Usage
dog = Dog("Buddy")
cat = Cat("Whiskers")

print(dog.speak())  # Output: Woof!
print(cat.speak())  # Output: Meow!

# Real-Time Use Case: A zoo management system where Animal is a base class and Dog and Cat are subclasses with specific behavior.