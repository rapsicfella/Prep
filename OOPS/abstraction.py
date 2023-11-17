
'''
Abstraction: 

Abstraction is used to hide the internal functionality of the function from the users. 
The users only interact with the basic implementation of the function, but inner working is hidden. 
User is familiar with that "what function does" but they don't know "how it does."

In simple words, we all use the smartphone and very much familiar with its functions such as camera, voice-recorder, call-dialing, etc., 
but we don't know how these operations are happening in the background. 
Let's take another example - When we use the TV remote to increase the volume. 
We don't know how pressing a key increases the volume of the TV. We only know to press the "+" button to increase the volume.
'''

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

    # Usage

circle = Circle(5)
print("Circle Area:", circle.area())  # Output: 78.5
# Real-Time Use Case: A graphics library where Shape is an abstract class, and Circle is a concrete class providing implementation.