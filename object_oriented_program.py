# Object Oriented Programming in Python
# Class

def cat(name):
    print (name)
cat('Buddy')

class Dog:
    """Model a dog"""
    def __init__(self, name, age, sound = "bark"):
        self.name = name
        self.age = age
        self.sound = sound
    def show_info(self):
        """Return the name of the Dog object"""
        return self.name

dog1 = Dog("Billy", 4)
print(dog1.show_info())

