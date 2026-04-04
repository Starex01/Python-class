# **Backend Engineering Class Two Assignment**

## 📌 Task:

### **1. Data types:Predict the output of the following code and print each variable.

name = "Ada" ## String
age = 12 ## Integer
height = 1.5 ## Float
is_student = True ## Boolean 

print(type(name))
print(type(age))
print(type(height))
print(type(is_student))

## What function should we use to check the data type of each variable above? Show an example with one.

### **2. String concatenation:Combine the code below to output `"John Doe"`

first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name
print(full_name)

### **3. Mathematical operations: Given
# Add, Subtract, Multiply and Divide a and b. Print the results.
a = 10
b = 3 
## Add
print(a + b)
#  subtract,
print(a - b)
#  multiply 
print(a * b)
#  divide a and b. Print the results.
print(a / b)


### **4. Floating point limitation: Floats can be inaccurate for money. Observe the weird result you get by running this:

a = 0.1
b = 0.2
print(a + b)

# Python provides a workaround to this limitation using the decimal module:

from decimal import Decimal

a = Decimal("0.1")
b = Decimal("0.2")


# Print the result of adding a and b.

### **5. Truthy or Falsy: What would be the result of printing each of these? Answer **True** for those that are truthy or **False** for falsy.

bool(0) # Falsy
bool(1) # Truthy
bool("") # Falsy
bool("Python") # Truthy
bool(0.0) # Falsy
bool(3.14) # Truthy
bool(False) # Falsy
bool(True) # Truthy


### **Deadline:**

## **Saturday 21 March, 2026 by 8pm WAT**