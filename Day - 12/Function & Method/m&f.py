# Function on Tuple 

# 1 - len()  --> it returns the number of items in the tuple. 
#2 - max()  --> it returns the largest item in the tuple.
#3 - min()  --> it returns the smallest item in the tuple.
#4 - sum()  --> it returns the sum of all items in the tuple.
#5 - sorted()  --> it returns a new sorted list from the items in the tuple.
#6 - any() --> it returns True if any item in the tuple is True.
#7 - all() --> it returns True if all items in the tuple are True.

# len()
tuple1 = (1, 2, 3, 4, 5)
print(len(tuple1)) # Output: 5

# max()
tuple2 = (1, 2, 3, 4, 5)
print(max(tuple2)) # Output: 5

# min()
tuple3 = (1, 2, 3, 4, 5)
print(min(tuple3)) # Output: 1

# sum()
tuple4 = (1, 2, 3, 4, 5)
print(sum(tuple4)) # Output: 15

# sorted()
tuple5 = (1, 5, 4, 2, 3)
print(tuple(sorted(tuple5)))  # Output: (1, 2, 3, 4, 5)


# any()
# Example 1 
tuple6 = (1, 2, 3, 4, 5)
print(any(tuple6)) # Output: True
# Example 2 
tuple7 = ()
print(any(tuple7)) # Output: False

# all()
# Example 1 
tuple7 = (1, 2, 3, 4, 5)
print(all(tuple7)) # Output: True
# Example 2
tuple8 = (1, 2, 3, 4, 5, 0)
print(all(tuple8)) # Output: False

# Method on Tuple

# 1 - index() --> it returns the index of the first item in the tuple with the specified value.
# 2 - count() --> it returns the number of times the specified value appears in the tuple.
# 3 - reverse() --> it reverses the order of the items in the tuple.
# 4 - sort() --> it sorts the items in the tuple.
# 5 - clear() --> it removes all items from the tuple.
# 6 - copy() --> it returns a shallow copy of the tuple.

# index()
tuple9 = (1, 2, 3, 4, 5)
print(tuple9.index(3)) # Output: 2

# count()
tuple10 = (1, 2, 3, 4, 5, 3, 2, 1)
print(tuple10.count(3)) # Output: 2

# reverse()
tuple11 = (1, 2, 3, 4, 5)
tuple11.reverse()
print(tuple11) # Output: (5, 4, 3, 2, 1)

# sort()
tuple12 = (1, 5, 4, 2, 3)
tuple12.sort()
print(tuple12) # Output: (1, 2, 3, 4, 5)

# clear()
tuple13 = (1, 2, 3, 4, 5)
tuple13.clear()
print(tuple13) # Output: ()

# copy()
tuple14 = (1, 2, 3, 4, 5)
tuple15 = tuple14.copy()
print(tuple15) # Output: (1, 2, 3, 4, 5)
