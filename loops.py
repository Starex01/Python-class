import time
# types of loops in python
# for loop
for number in range(1, 11):
    print(number, end=" ")
    #time.sleep(0.2)

print()
name = "Python 23"
for character in name:
    print(character)
    time.sleep(0.2)

print()
for num in range(1,5):
    if num == 3:
        continue
    print(num)

# while loop
counter = 0
while counter < 3:
    print("i Love python", end=" ")
    counter = counter + 1
    #time.sleep(0.2)

print()
# break and continue statement
number = 1
while True:
    if number == 11:
        break
    elif number == 7:
        number = number + 1
        continue
    else:
        print(number)
        number = number + 1

# number = 1
# while number < 11:
#     print(number)
#     number += 1


