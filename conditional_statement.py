# input user
# If, else, elif statement

name = input("Enter your name? ")
age = int(input("Enter your age? "))

print (type(age))

if age >= 18:
    if age < 201:
        print(f"Hello {name}, You are eligible to vote.")
    else:
        print(f"Hello {name}, You are way above the age to vote: {age} Years Old.")    
elif age < 18 and age > 0:
    print(f"Hello {name}, Minors are not allowed to vote.")
else:
    print(f"Hello {name}, You have entered an invalid age: {age}. Please enter a valid age.")

