# Assignment
# Write a program that checks if a number is positive, negative or zero.
# Your program should output:
# "Positive number" for positive numbers
# "Negative number" for negative numbers
# "Zero" for zero
# Hint: Use the input function to accept numbers

num = float(input("Enter a number: "))
while True:
    if num > 0:
        print("Positive number")
    elif num < 0:
        print("Negative number")
    else:
        print("Zero")
    break
