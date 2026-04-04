# 1. Task
#Create a list called fruits with at least 5 different fruits.
#Print the first fruit
#Print the last fruit
#Print the third fruit
#Goal: Practice indexing ([0], [-1], etc.)

fruits = ['apple', 'banana', 'orange', 'grape', 'mango']
#Print the first fruit
print(fruits[0])
#Print the last fruit
print(fruits[4])
#Print the third fruit
print(fruits[2])

# 2. Task
#Given the list:
# numbers = [10, 20, 30, 40, 50, 60, 70]
# Print the first 3 numbers
# Print the last 3 numbers
# Print everything except the first and last number
#Goal: Practice slicing ([start:end])

numbers = [10, 20, 30, 40, 50, 60, 70]

# Print the first 3 numbers
print(numbers[0:3])
# Print the last 3 numbers
print(numbers[4:7]) 
# Print everything except the first and last number
print(numbers[1:6])


# 3. Task
# Create a list:
# colors = ["red", "blue", "green"]
# Add "yellow" to the end
# Insert "purple" at index 1
# Change "green" to "black"
# Goal: Use .append(), .insert(), and indexing

colors = ["red", "blue", "green"]
# Add "yellow" to the end
colors.append("yellow")
print(colors)

# Insert "purple" at index 1
colors.insert(1, "purple")
print(colors)

# Change "green" to "black"
colors[3] = "black"
print(colors)

# 4. Task: Removing Items
# Given:
# animals = ["dog", "cat", "rabbit", "lion", "cat"]
# Remove the first "cat"
# Remove "lion" using a method
# Remove the last item in the list
# Goal: Use .remove() and .pop()

animals = ["dog", "cat", "rabbit", "lion", "cat"]

# Remove the first "cat"
animals.remove("cat")
print(animals) 

# Remove "lion" using a method
animals.pop(-2)
print(animals)

# Remove the last item in the list
animals.pop()
print(animals)

# 5. Task
# Create a list of numbers:
# scores = [50, 20, 80, 40, 90]
# Sort the list in ascending order
# Sort the list in descending order
# Reverse the list
# Goal: Use .sort() and .reverse()

scores = [50, 20, 80, 40, 90]

# Sort the list in ascending order
scores.sort()
print(scores)


# Sort the list in descending order
scores.sort(reverse=True)
print(scores)

# Reverse the list
scores.reverse()
print(scores)
