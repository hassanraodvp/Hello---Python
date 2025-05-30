# List 
# A list is a collection which is ordered and changeable. Allows duplicate members.

# List is one of 4 built-in data types in Python used to store collections of data, the other 3 are # 1 - Tuple, # 2 - Set, and # 3 - Dictionary, all with different qualities and usage.

# Lists are created using square brackets:

# Example 1
this_list = ["apple", "banana", "cherry"]
print(this_list) # Output: ['apple', 'banana', 'cherry']
# List Items
# List items are ordered, changeable, and allow duplicate values.
# List items are indexed, the first item has index [0], the second item has index [1] etc.

# ordered - Maintains the order of the items in the list.
# Example
num_list = [1, 2, 3, 4, 5]
print(num_list) # Output: [1, 2, 3, 4, 5]
# changeable - Allows you to change, add, and remove items in a list after it has been created.
# Example
this_list_item = ["apple", "banana", "cherry"]
print(this_list_item) # Output: ['apple', 'banana', 'cherry']
this_list_item[1] = "orange"
print(this_list_item) # Output: ['apple', 'orange', 'cherry']
# allow duplicate values - Since lists are indexed, lists can have items with the same value.
# Example
this_list2 = ["apple", "banana", "cherry", "apple", "cherry"]
print(this_list2)

# Heterogenous List
# Lists can contain items of different types:
#Example
list = [1, "Banana", 2, "Apple", 3, True, 4.4,]
print(list)



