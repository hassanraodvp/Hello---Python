# Example 1
for var1 in range(1, 11):
    print("Outer loop:", var1)
    for var2 in range(3, 5+1):
        print("Inner loop variable is:", var1 * var2)
    print("Outer loop:", var1)    

# Example 2     
n = 7
for outer in range(1, n+1):
    for inner in range(outer):
        print("*", end="")
    print()    
