# The Process of converting of one data type (str, int, float) to another is called type conversion. 
# Python has two type of conversion 
# 1. Implicit Type Conversion
# 2. Explicit Type Conversion

# Implicit Type Conversion
# In this type of conversion, Python automatically converts one data type to another data type.
num_int = 123
num_flo = 1.23

num_new = num_int + num_flo

print("datatype of num_int:",type(num_int))
print("datatype of num_flo:",type(num_flo))

print("Value of num_new:",num_new)
print("datatype of num_new:",type(num_new))

# Explicit Type Conversion
# In this type of conversion, Python converts the data type of an object to required data type.
num_int = 123
num_str = "456"

print("Data type of num_int:",type(num_int))
print("Data type of num_str before Type Casting:",type(num_str))

num_str = int(num_str)
print("Data type of num_str after Type Casting:",type(num_str))

num_sum = num_int + num_str

print("Sum of num_int and num_str:",num_sum)