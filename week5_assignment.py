## Section A: Multiple Choice (3 questions)
# 1. Which data type is mutable?
# A. Tuple
# B. String
# C. List
# D. Integer
# Answer: C. List 

# 2. What will this code output?
numbers = [1, 2, 3]
numbers.append([4, 5, 6])
print(len(numbers))
# A. 3
# B. 4
# C. 5
# D. Error
# Answer: B. 4

# 3. Which keyword is used to send a value back from a function?
# A. print
# B. return
# C. yield
# D. def
# Answer: B. return

# 4. What is the difference between a list and a tuple?
# List are mutable while Tuple are immutable
# Example 
my_list = [1, 2, 3]     # can change
my_tuple = (1, 2, 3)    # cannot change
print(my_list)
print(my_tuple)

# 5. What will this code print?
def greet(name):
    print("Hello", name)
result = greet("Ada")
print(result)
# A. Hello Ada
# B. None - result is not defined

# 6. Write the syntax to create a dictionary with keys "name" and "age".
person = {
    "name": "John",
    "age": 25
}
print(person)

# 7. Write a function called add_numbers that takes two numbers and returns their sum
def add_numbers(a, b):
    return a + b
print(add_numbers(5, 3))

# For questions 8&9, given the list below, write code to
numbers = [2, 4, 6, 8, 10]

# 8. Add 12 to the end of the list
numbers.append(12)
print(numbers)

# 9. remove 4 from the list
numbers.remove(4)
print(numbers)

# 10. Given the dictionary:
student = {"name": "John", "age": 12, "grade": "A"}
# Print the student’s name
print(student["name"])
# Add a new key "school" with value "Greenwood"
student["school"] = "Greenwood"
print(student)


    



# def student(name, age, school="ABC School"):
#     """ Return a string with the student's information. """
#     return f"{name} is {age} years old and attends {school}."

# print(type(student("Alice", 20)))