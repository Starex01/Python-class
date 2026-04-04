def greet(name):   
    """ Greet the person with the given name. """ # """ is used for docstring, which is a string literal that occurs as the first statement in a module, function, class, or method definition. It is used to document the purpose and usage of the function."
    return f"hello {name}";

# calling the function greet with the argument "Alice" and printing the result. The output will be "hello Alice".
print(greet("Alice"))

# function is greet while name is the parameter. "hello {name}" is the return value of the function. The f before the string indicates that it is a formatted string literal, which allows you to include expressions inside curly braces {} that will be evaluated at runtime and included in the resulting string. In this case, {name} will be replaced with the value of the name parameter when the function is called.

# def greet_from_list():
#     """ Greet each person in the list of names. """
#     names = ["Alice", "Bob", "Charlie"] # This line is not necessary, as the function should use the names passed as an argument. It will override any input provided to the function.
#     return f"Hi {names[1]}"
# print(greet_from_list())

def square(num):
    """ Return the square of a number. """
    return num ** 2 ## two asterisks (**) is the exponentiation operator in Python, which raises the number on the left to the power of the number on the right. In this case, num ** 2 calculates the square of num.
print(square(5))

fruits = ["apple", "banana", "cherry"]
print(len(fruits)) # This line will print the length of the fruits list, which is 3, because there are three items in the list.
print(len("Hello World")) # This line will print the length of the string "Hello, World!", which is 13, because there are 13 characters in the string (including spaces and punctuation).
print(len([2, 4, 7])) # This line will print the length of the list [2, 4, 7], which is 3, because there are three items in the list.

def nam(name, msg = "Hello"):
    """ Greet the person with the given name and message. """
    return f"{msg} {name}"
print(nam("Alice")) # This line will call the nam function with the argument "Alice" and print the result. Since the msg parameter has a default value of "Hello", the output will be "Hello Alice".

def student(name, age, school="ABC School"):
    """ Return a string with the student's information. """
    return f"{name} is {age} years old and attends {school}."
print(student("Tolani", age=15)) # This line will call the student function with the arguments "Tolani" and age=15, and print the result. Since the school parameter has a default value of "ABC School", the output will be "Tolani is 15 years old and attends ABC School."
# school is default argument, positional argument is name and keyword argument is age. Positional arguments are arguments that are passed to a function in the correct positional order. Keyword arguments are arguments that are passed to a function by explicitly specifying the parameter name and value. Default arguments are arguments that have a default value specified in the function definition, and can be omitted when calling the function.


score = 0
answers = ["science", "English", "history"]
def mark():
    global score
    
    for answer in range(len(answers)): # This line will iterate over the range of the length of the answers list, which is 3. The variable answer will take on the values 0, 1, and 2 in each iteration of the loop. However, it would be more appropriate to iterate directly over the answers list using a for loop like this: for answer in answers:
        score += 1 # This line will cause an error because score is defined outside the function and is not declared as a global variable. To modify the score variable inside the function, you should declare it as global like this: global score    
    return score
print(mark())



