# Ordered data structure: A list is an ordered data structure, which means that the elements in a list are stored in a specific order. We can access the elements of a list using their index, which starts at 0. For example, to access the name at index 2, we can do the following:
names = ['Suleiman', 'Abraham', 'Joel', 'Johnson', 'Opeyemi', 'Abraham', 'Samuel', 'John']
print(names)

# Mutable data structure: We can change the value of an element in a list by accessing its index and assigning a new value to it. For example, to change the name at index 3 to 'Oduyomi', we can do the following:
names[3] = 'Oduyomi'
print(names)

# Sliceable data structure: We can access a range of elements in a list using slicing. For example, to access the first three names in the list, we can do the following:
print(names[0:3]) # This will print the names at index 0, 1, and 2.
print(names[0:2]) # This will print the names at index 0, and 1.
print(names[0:3:1]) # This will print the names at index 0, 1, and 2 with a step of 1 (which means it will print every element in the range).
print(names[0:3:2]) # This will print the names at index 0, 2.
print(names[1:6:3]) # This will print the names at index 1, 4.
print(names[2:6:4]) # This will print the names at index 2, 6.

# Reverse slice: We can also reverse a list using slicing. For example, to reverse the list of names, we can do the following:
print('Reversed list')
print(names[::-1]) # This will print the names in reverse order.
print(names[-2:-5:-1]) # This will print the names at index -2, -3, and -4 in reverse order (which means it will print the names at index 6, 5, and 4).
print(names[-5:0:-1]) # This will print the names at index -5, -6, -7, and -8 in reverse order (which means it will print the names at index 3, 2, 1, and 0).



# Add items to a list: We can add items to a list using the append() method. For example, to add the name 'Adewale' to the end of the list, we can do the following:
names.append('Deborah')
print(names)
# Insert an item at a specific index: We can insert an item at a specific index using the insert() method. For example, to insert the name 'Adewale' at index 2, we can do the following:
names.insert(0, 'Adesope')
names.pop() # This will remove the last item in the list, which is 'Deborah'.
names.pop(-1) # This will also remove the last item in the list, which is 'Deborah'.
names.remove('Abraham') # This will remove the first occurrence of 'Abraham' from the list.
print(names)

reversed_list = names.reverse() # This will reverse the list in place, which means it will change the original list.
 # This will print the reversed list.
