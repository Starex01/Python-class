# 1. Create a parent class called Animal
# The class should have __init__ method that takes name & a method speak() that prints "This Animal makes a sound"

class Animal:
    """Model an animal"""
    def __init__(self, name):
        self.name = name
    def speak(self):
        """Amimal sound"""
        return(f"{self.name} makes sound")
    def describe(self):
        """Return the description of the animal"""
        return f"This is an animal named {self.name}"
    

animal = Animal("Dog")
print(animal.speak())
animal2 = Animal("Cat")
print(animal2.speak())
print(animal.describe())

# 2. Create two subclasses: Dog & Cat

class Dog(Animal):
    pass
class Cat(Animal):
    pass

dog = Dog("Dog")
print(dog.speak())

cat = Cat("Cat")
print(cat.speak())

# 3. Method Overriding & super()
# Modify your classes:
# Add a method describe() in Animal to return "This is an animal named {name}"
# Override describe() in Dog & Cat
# Use super() to call the parent class method
# Add extra info

class Dog(Animal):
    """Model a dog"""
    def __init__ (self, name):
        super().__init__(name)
    def describe(self):
        """Override describe() in Dog"""
        return super().describe()
    def extra_info(self):
        """Add extra info"""
        return f"It is a loyal animal"

dog_1 = Dog("Dog")
print(dog_1.describe())
print(dog_1.extra_info())

class Cat(Animal):
    """Model a cat"""
    def __init__ (self, name):
        super().__init__(name)
    def describe(self):
        """Override describe() in Cat"""
        return super().describe()
    def extra_info(self):
        """Add extra info"""
        return f"It is an independent animal"

cat_1 = Cat("Cat")
print(cat_1.describe())
print(cat_1.extra_info())

# 4. Polymorphism in Action
# Create a function:

def animal_sound(animal):
    return animal.speak()

# Pass different objects (Dog, Cat) into this function
# Show that same function behaves differntly
dog_1 = Dog("Dog")
print(animal_sound(dog_1))
cat_1 = Cat("Cat")
print(animal_sound(cat_1))
    
