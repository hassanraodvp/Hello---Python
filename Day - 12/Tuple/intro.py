# Tuple :
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.

#Example of tuple:
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple)
print(type(my_tuple))

# Accessing elements of tuple:
print(my_tuple[0])  # Output: 1
print(my_tuple[1:3]) # Output: (2, 3)

# Concatenation of tuples: 
tuple1 = (1, 2, 3, 4, 5, 6, 7)
tuple2 = (8, 9, 10, 11, 12, 13, 14)
tuple3 = tuple1 + tuple2
print(tuple3)

# Repetition of tuples:
tuple4 = (1, 2, 3, 4, 5, 6, 7)
tuple5 = tuple4 * 3
print(tuple5)

# Membership of tuples:
tuple6 = (1, 2, 3, 4, 5, 6, 7)
print(4 in tuple6)

# Iterable in Tuple 
tuple7 = (1, 2, 3, 4, 5, 6, 7)
for i in tuple7:
    print(i)

# Immutable     
tuple8 = (1, 2, 3, 4, 5, 6)
tuple8[0] = 10
print(tuple8)

