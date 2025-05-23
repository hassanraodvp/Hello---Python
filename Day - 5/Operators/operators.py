# Types of Operators:
# 1. Arithmetic Operators (+,-,*,/,%,**,//)
num1 = 10 # Here 10 is Operands
num2 = 20 # Here 20 is Operands
result = num1 + num2 # Here + is Operator
print(result)
# 2. Assignment Operators (=,+=,-=,*=,/=,%=)

# 3. Comparison Operators (==,!=,>,<,>=,<=)

# 4. Logical Operators (and,or,not)

# 5. Identity Operators (is,is not)
a = 10
b = 20
id(a)
id(b)
print(id(a))
print(id(b))
print(a is b) # False
print(a is not b) # True
print(type(a) is float) # False
print(type(a) is not float) # True

# 6. Membership Operators (in,not in)
name = "Python"
print("P" in name) # True
print("p" not in name) # True

integer = [1,2,3,4,5]
print(3 in integer) # True
print(3 not in integer) # False

# 7. Bitwise Operators (&,|,^,~)

print(6 / 2 + 3 ** 4)
print(2 ** 3 ** 2) # 512
