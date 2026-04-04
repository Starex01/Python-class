print("Adewunmi Abraham")

first_car = "Toyota"
second_car = "Honda"    
third_car = "Ford"

# Data Types in Python are integers, strings, floats, booleans 

print(first_car)
print(second_car)
print(third_car)    

all_cars = first_car + ", " + second_car + ", " + third_car
print(all_cars)

#floats (Decimal numbers)
amount = 100.50
tax_rate = 0.07
cgpa = 3.5
weight = 150.75
height = 5.9

print(amount + 1)
print(tax_rate * 100)

# use decimal module to bypass floating point limitations
from decimal import Decimal
print(Decimal('0.1') + Decimal('0.2')) 

 # booleans (True or False)
is_raining = True
is_sunny = False

print(True + True)
print (False - 2)

# Type conversion
# Integer to String
age = 25
print(type(age))
stringify_age = str(age)
print(type(stringify_age))

# String to Integer
height = "5"
str_to_int = int(height)
print(str_to_int + 2)

# name = "CR"
# name_to_int = int(name)  # This will raise a ValueError because "CR7" cannot be converted to an integer
# print(name_to_int)

# empty string to boolean
empty_string = ""
print(bool(empty_string))  # This will print False because an empty string is considered False in

first_name = "Adewunmi"
print(bool(first_name))  # This will print True because a non-empty string is considered True in Python

if True:
    print("Truthy")
else:    
    print("Falsy")

zero = 0
print(bool(zero))  # This will print False because 0 is considered False in Python
stringify_zero = str(zero)
print(bool(stringify_zero))  # This will print True because a non-empty string is considered 


print(bool(False))
print(bool("False"))

f_name = "Adewunmi"
l_name = "Abraham"
print(f_name + " " + l_name)
