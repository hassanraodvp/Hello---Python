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

#Method in List
list4 = [1,3,2,4,6,5,7,8,9, 99]
# 1 - list.append() - Add an element at the end of the list
list4.append(100)
print(list4) # [1, 3, 2, 4, 6, 5, 7, 8, 9, 99, 100]

# 2 - list.clear() - Remove all the elements from the list
list4.clear()
print(list4) # []

# 3 - list.copy() - Return a copy of the list
list4 = [1,3,2,4,6,5,7,8,9, 99]
list5 = list4.copy()
print(list5) # [1, 3, 2, 4, 6, 5, 7, 8, 9, 99]

#4 - list.extend() - Add the elements of a list (or any iterable), to the end of the current list
list5 = [666, 7777, 888]
list4.extend(list5)
print(list4) # [1, 3, 2, 4, 6, 5, 7, 8, 9, 99, 100, 200, 300, 666, 7777, 888]
list4.extend([100,200,300])
print(list4) # [1, 3, 2, 4, 6, 5, 7, 8, 9, 99, 100, 200, 300]

# 5 - list.index() - Return the index of the first element with the specified value
list4 = [1,3,2,4,6,5,7,8,9, 99]
print(list4.index(9)) # 8

# 6 - list.insert() - Add an element at the specified position
list4.insert(0, 9009)
print(list4) # [9009, 1, 3, 2, 4, 6, 5, 7, 8, 9, 99]

# 7 - list.pop() - Remove the element at the specified position
list4.pop(0)
print(list4) # [1, 3, 2, 4, 6, 5, 7, 8, 9, 99]

# 8 - list.remove() - Remove the item with the specified value
list4.remove(99)
print(list4) # [1, 3, 2, 4, 6, 5, 7, 8, 9]

# 9 - list.reverse() - Reverse the order of the elements in the list
list4.reverse()
print(list4) # [9, 8, 7, 5, 6, 4, 2, 3, 1]

# 10 - list.count() - Return the number of elements with the specified value
list6 = [1,3,2,9,4,6,5,9,9,7,8,9, 99]
print(list6.count(9)) # 4

# 11 - list.sort() - Sort the list
list4.sort()
print(list4) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 99]
