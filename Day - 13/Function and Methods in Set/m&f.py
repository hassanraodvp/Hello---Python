# Function on Set
#1 - len() it returns the number of elements in the set
#2 - max() it returns the maximum element in the set
#3 - min() it returns the minimum element in the set
#4 - sum() it returns the sum of all elements in the set
#5 - any() it returns True if at least one element of the set is true
#6 - all() it returns True if all elements of the set are true

# len()
set1 = {1,2,3,4,5}
print(len(set1)) # Output: 5

# max()
set2 = {1,2,3,4,5, 99}
print(max(set2)) # Output: 99

# min()
set3 = {1,2,3,4,5}
print(min(set3)) # Output: 1

# sum()
set4 = {1,2,3,4,5}
print(sum(set4)) # Output: 15

# any()
# example 1
set5 = {1, 2, 3, False} # if any element is True then it will return True
print(any(set5)) # Output: True
#example 2
set6 = {0, 0, 0, 0} # if all elements are False then it will return False
print(any(set6)) # Output: False

# all()
# example 1
set7 = {1,2,3,4,5}
print(all(set7)) # Output: True
#example 2
set8 = {1,2,3,4,0}
print(all(set8)) # Output: False
#example 3
set9 = {1,2,3,4,5,6, False}
print(all(set9)) # Output: False


# Methods on Set
#1 - add() it adds an element to the set
#2 - clear() it removes all elements from the set
#3 - copy() it returns a shallow copy of the set
#4 - difference() it returns a set with elements in the set but not in the other set
#5 - difference_update() it removes elements from the set that are also in the other set
#6 - discard()/remove() it removes an element from the set if it is a member
#7 - pop() it removes and returns an arbitrary element from the set

# add()
set10 = {1,2,3,4,5}
set10.add(6)
print(set10) # Output: {1, 2, 3, 4, 5, 6}

# clear()
set11 = {1,2,3,4,5}
set11.clear()
print(set11) # Output: set()

# copy()
set12 = {1,2,3,4,5}
set13 = set12.copy()
print(set13) # Output: {1, 2, 3, 4, 5}

# difference()
set14 = {1,2,3,4,5}
set15 = {4,5,6,7,8}
set16 = set14.difference(set15)
print(set16) # Output: {1, 2, 3}

# difference_update()
set17 = {1,2,3,4,5}
set18 = {4,5,6,7,8}
set17.difference_update(set18)
print(set17) # Output: {1, 2, 3}

# discard()/remove()
set19 = {1,2,3,4,5}
set19.discard(4)
print(set19) # Output: {1, 2, 3, 5}
set20 = {1,2,3,4,5}
set20.remove(4)
print(set20) # Output: {1, 2, 3, 5}

# pop()
set21 = {1,2,3,4,5}
set21.pop()
print(set21) # Output: {2, 3, 4, 5}