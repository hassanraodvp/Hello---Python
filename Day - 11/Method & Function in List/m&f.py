# Function Vs Method in Python

# Function - A block of code that does a particular operation and returns a result.
# Method - A method is a function that is associated with an object.

# Function - Called on an object or variable
# Method - Needs an object/variable to work on 

# Function - len()
# Function - max()
# Function - min()
# Function - sum()
# Function - sorted()

# Method - list.sort()
# Method - list.append()
# Method - list.pop()
# Method - list.count()
# Method - list.reverse()
# Method - list.clear()
# Method - list.copy()
# Method - list.extend()
# Method - list.index()
# Method - list.insert()
# Method - list.remove()

# Function in LIst 
# 1 - len() - Tell the length of list
list1 = [1,3,2,4,6,5,7,8,9, 99]
print(len(list1))
# 2 - max() - Tell the maximum number in list
print(max(list1))  
# 3 - min() - Tell the minimum number in list
print(min(list1))
# 4 - sum() - Sum of all the number in list
print(sum(list1))
# 5 - sorted() - Sort the list
print(sorted(list1))
# 6 - list.sort() - Sort the list
list1.sort()
print(list1)
# 7 - any() - it return true if any one of the items is true
print(any(list1))
# 8 - all() - it return true if all the items is true
list2 = [1,2,3,4,5,6,7,8,9, True]
list3 = [1,2,3,4,5,6,7,8,9, False]
print(all(list2))
print(all(list3))
