# Example 1 
a = '7' # '7' * 3  →  '7' + '7' + '7' + '7' + '7' + '7' + '7' + '7'  →  '77777777'
b = 8
print(a * b) # Output: 777

# Example 2 

name = 'JohnDoe'
name2 = "Kale"

print(name + name2) # Output: JohnDoeKale

print(name + " " + name2) # Output: JohnDoe Kale

# Example 3
num1 = input("Enter a number: ") # 22
num2 = input("Enter another number: ") #20
print(num1 + num2) # Output: 2220 (Because by default input is string)

# Example 4
num1 = int(input("Enter a number: ")) # 22
num2 = int(input("Enter another number: ")) #20
print(num1 + num2) # Output: 42

# Slicing 
# Example 1
name = "JohnDoeHelieKimbertly"
print(name[0:4]) # Output: John
print(name[5:9]) # Output: DoeH
print(name[10:15]) # Output: Kim
print(name[16:]) # Output: bertly
# Example 2
name = "JohnDoeHelieKimbertly"
print(name[-1]) # Output: y
print(name[-2]) # Output: l
# Example 3 
num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(num[:]) # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(num[::]) # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(num[2:2]) # Output: []
print(num[2::])  # Output: [3, 4, 5, 6, 7, 8 , 9, 10]
print(num[1:]) # Output: [2, 3, 4, 5, 6, 7, 8, 9, 10]
print(num[2:7:]) # Output: [3, 4, 5, 6, 7] 
print(num[2:7:2]) # Output: [3, 5, 7]
print(num[2:]) # Output: [3, 4, 5, 6, 7, 8, 9, 10]
print(num[:7:]) # Output: [1, 2, 3, 4, 5, 6, 7]
print(num[:7:2]) # Output: [1, 3, 5, 7]