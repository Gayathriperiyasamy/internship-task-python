class Animal:
    def __init__(self, species):
        self.species = species

    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def __init__(self, breed):
        super().__init__("Dog")
        self.breed = breed

    def speak(self):
        print("Woof!")

dog = Dog("Labrador")
print(f"Species: {dog.species}, Breed: {dog.breed}")
dog.speak()
