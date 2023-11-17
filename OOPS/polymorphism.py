class Animal:
    def __init__(self, animal_id) -> None:
        self.animal_id = animal_id
    def speak(self):
        print('I am an animal')

class Dog(Animal):
    def __init__(self, animal_id, dog_id) -> None:
        super().__init__(animal_id)
        self.dog_id = dog_id

    def speak(self):
        super().speak()
        print('I am a dog')


obj1 = Dog(23, 67)

obj1.speak()