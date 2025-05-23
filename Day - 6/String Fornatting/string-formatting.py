# Example - 1 
num = 8978876 / 3444
print("The result is %2.26f" %(num))
num = 89 / 3
print("The result is %.2f" %(num))

# Example - 2
name = "John"
age = 25
print("Hello, my name is {} and I am {} years old.".format(name, age))
print(f"Hello, {name}. You are {age} years old.")
# print("Yes, I'm " + age + " years old")  # <-- This will cause an error
print("Yes, I'm " + str(age) + " years old")  

# Example - 3 
pi = 3.141592653589793
print("The Value of pi rounded to 2 decimal places is %.2f" %pi)
print("The Value of pi rounded to 4 decimal places is {:.4f}".format(pi))
print(f"The Value of pi rounded to 6 decimal places is {pi:.6f}")

# Example - 4 
income = 1000
tax = 300
print(f"The Final income is {income}, after tax is {income - tax}")