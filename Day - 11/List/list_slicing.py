# Original list
my_list = [1, "Apple", 2, 3, "Banana", 4, 5, True, 6, "Mango", 7, 8, 3.14, 9, "Cherry", 10]

# Slicing
print(my_list[0:5])     # [1, "Apple", 2, 3, "Banana"]
print(my_list[5:10])    # [4, 5, True, 6, "Mango"]
print(my_list[10:15])   # [7, 8, 3.14, 9, "Cherry"]
print(my_list[2:10:2])  # [2, 'Banana', 5, 6]
print(my_list[::2])     # [1, 2, 'Banana', 5, 6, 7, 3.14, 'Cherry']
print(my_list[::-1])    # reversed list
print(my_list[::3])     # every 3rd element

# Reverse list in place
my_list.reverse()
print(my_list)

# Sorting another list
list2 = [2, 3, 1, 9, 6, 7, 4, 5]
list2.sort()
print(list2)

# Insert item
my_list.insert(0, "Orange")
print(my_list)

# Remove an item
my_list.remove("Cherry")
print(my_list)

# Append item (do NOT assign the result of append())
my_list.append("Orange")
print(my_list)

# Pop item (again, do not assign result of pop() unless you want the popped value)
my_list.pop()
print(my_list)

# Pop first element
my_list.pop(0)
print(my_list)

# Add two lists
my_list = my_list + [3, 4, 5]
print(my_list)

# Add more items with +=
my_list += [6, 7, 8]
print(my_list)

# Print length
print(len(my_list))  
