# Classes and Objects

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_details(self):
        print(f'{self.name} is {self.age} years old ')


    
student1 = Student('harsha', 23)
student1.display_details()
# Real-Time Use Case: A car dealership system where each car is represented as an object of the Car class.
