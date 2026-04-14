# Object Oriented Programming in Python

def cat(name):
    print (name)
cat('Buddy')

# Class is a blueprint for creating objects. An object is an instance of a class. A class can have attributes and methods. Attributes are variables that belong to a class, while methods are functions that belong to a class. We can create multiple objects from a class, and each object can have different values for the attributes.
class Dog:
    """Model a dog"""
    def __init__(self, name, age, sound = "bark"):
        self.name = name
        self.age = age
        self.sound = sound
    def show_info(self): # This method is used to display the information of the Dog object. It takes no parameters and returns a string that contains the name, age, and sound of the dog.
        """Return the name of the Dog object"""
        return self.name

dog1 = Dog("Billy", 4)
print(dog1.show_info())

class Student:
    """Model a student"""
    def __init__(self, name, age, grade): # __init__ is the class constructor method, which is called when a new instance of the class is created. It initializes the attributes of the class with the values passed as arguments when creating an instance of the class. In this case, it initializes the name, age, and grade attributes of the Student class.
        self.name = name
        self.age = age
        self.grade = grade
    def info(self):
        """Return Information about a Student"""
        return f"{self.name} is {self.age} years old and is in grade {self.grade}."
    def create_username(self):
        """Create username for the student"""
        username = self.name + str(self.age)
        return username.lower() # This line will convert the username to lowercase using the lower() method, which is a string method that returns a copy of the string with all characters converted to lowercase. This is often done to ensure that usernames are case-insensitive and consistent in format.
    def change_name(self):
        """Change the name of the student"""
        old_name = self.name
        new_name = old_name.replace(self.name, "Joyce") # This line will replace the old name with the new name "Joyce" using the replace() method, which is a string method that returns a copy of the string with all occurrences of a specified substring replaced with another substring. In this case, it replaces the current name of the student with "Joyce".
        self.name = new_name
        return self.name
    # def change_name(self, new_name):
    #     """Change the name of the student"""
    #     self.name = new_name

student1 = Student("Joy", 11, 9)
print(student1.info())
print(student1.create_username())
student1.change_name()
print(student1.info())

# 2. Emcapsulation: Encapsulation is the process of hiding the internal details of an object and only exposing a public interface. This is done to protect the data and ensure that it is not modified in an unintended way. In Python, we can use private attributes and methods to achieve encapsulation. Private attributes and methods are defined with a double underscore prefix (__) and are not accessible from outside the class.
is_tall = False
T = True + True
print(is_tall)
print(T)

class Animal:
    pass
class Dog(Animal): # Dog is a sub class of Animal, which means that it inherits all the attributes and methods of the Animal class. This is an example of inheritance, which is a fundamental concept in object-oriented programming that allows a new class to be created based on an existing class, inheriting its attributes and behaviors while allowing for additional features or modifications.
    pass
class Goat(Animal):
    pass

dog = Dog()
goat = Goat()

print(dog)

