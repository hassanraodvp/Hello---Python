# Syntax Error occur: 
# Example 1: Misspelling 'def' as 'dfe'
dfe my_function():  # Error: Should be 'def'
    print("Hello")

# Example 2: Misspelling 'for' as 'fro'
fro i in range(5):  # Error: Should be 'for'
    print(i)


# Example 1: Using assignment (=) instead of equality (==)
if x = 5:  # Error: Should be 'if x == 5:'
    print("x is 5")

# Example 2: Using wrong operator for string concatenation
name = "John"
age = 25
info = name + age  # Error: Can't concatenate str + int (use str(age))
# Example 1: Missing closing parenthesis in print
print("Hello, World"  # Error: Missing closing ')'

# Example 2: Missing parenthesis in function call
def greet(name):
    return f"Hello, {name}"
    
message = greet("Alice"  # Error: Missing closing ')'