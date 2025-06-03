# Sets 
# A set is unordered, no duplicates allowed, heterogenous & can't contain natural objects like (list, tuple, dict, etc.)
# immutable
# A set is useful for performing mathematical operations like union, intersection, and difference.

# unordered mean 
set1 = [5,3,4,1,2]
# no duplicates allowed
set2 = {1,2,3,4,5}  # we can't write like set2 = {1,2,3,3,4,5,5}
# heterogenous means 
set3 = {1,2,3,4,5,'a','b','c'}
# can't contain natural objects like (list, tuple, dict, etc.)
# set4 = {[1,2,3],{1,2,3},(1,2,3),{1:2,3:4}} # we can't write this.

#immutable means 
# set5 = {1,2,3,4,5}
# set5[0] = 10 # we can't write this.

# Union of Set 
set5 = {1,2,3,4,5}
set6 = {4,5,6,7,8}
result = set5 | set6
result2 = set5.union(set6) # we can also use union() method
print(result)
print(result2)

# Intersection of Set 
set7 = {1,2,3,4,5}
set8 = {4,5,6,7,8}
result3 = set7 & set8 
result4 = set7.intersection(set8) # we can also use intersection() method
print(result3)
print(result4)

# Difference of Set
set9 = {1,2,3,4,5}
set10 = {4,5,6,7,8}
result5 = set9 - set10
result6 = set9.difference(set10) # we can also use difference() method
print(result5)
print(result6)

