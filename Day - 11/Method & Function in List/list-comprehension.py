# Method - 1
list = []

for num in range(1, 15 + 1, 2):
    list.append(num)
print(list)
# Method - 2
list1 = [i for i in range(1, 15 + 1, 2)]
print(list1)

# Another Example 
list2 = [i for i in "Hassan" if i not in  "aeiou"]
print(list2)

# Another Example
list3 = [i for i in range(1, 100 + 1) if i % 2 == 0]
print(list3)

# Another Example
list4 = [i for i in range(1, 100 + 1) if i % 2 == 0 and i % 3 == 0]
print(list4)

# Another Example
list5 = [num if num % 2 == 0 else num +100 for num in range(1, 10 + 1)]
print(list5)