# Q:  Range() Function 
# Ans: Range Function is and inbuilt function in python which is used to generate a sequence of numbers (List or tuple).
# Syntax: range( Start, Stop, Step)
# Start: The starting number of the sequence.
# Stop: The end number of the sequence.
# Step: Difference between each number in the sequence.

# Example:

# Using range() function to generate a sequence of numbers

# Using range() function to generate a sequence of numbers from 1 to 5

for i in range(1, 6):
    print(i)

for l in range(1, 5 + 1):
    print(l)

result = []
for k in range(1, 15 + 1, 3):
    result.append(k)
print(result)


list = []
for value in range(1 , 8 , -2):
    list.append(value)
print(list)    

list2 = []
for value2 in range(8 , 1 , -2):
    list2.append(value2)
print(list2)    

# Important Note: 
# Range Does't support the fraction/decimal number
# e.g 

# for number in range (1 , 10 , 2.5):
#     print(number)

# for number2 in range (1 , 10.5 , 2):
#     print(number2)

# Program: Take input from user and print the sum of the numbers from 1 to the input number.
# Solution:
numInput = int(input("Enter the Num: "))
result = 0
for i in range(1 , numInput + 1):
    result += i
print(result)
