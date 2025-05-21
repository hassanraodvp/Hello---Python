# Few Imp Pints regarding to python data types 
# 1 - Data type in Python are dynamic 
# 2 - Size of data type in Python is dynamically managed 
# 3 - Data Types in Python are bounded 

a = 10
print(type(a))  # <class 'int'>

b = 10.5
print(type(b))  # <class 'float'>

c = 10 + 5j
print(type(c))  # <class 'complex'>

d = "Hello"
print(type(d))  # <class 'str'>

e = True
print(type(e))  # <class 'bool'>

f = ["apple", "banana", "cherry"]
print(type(f))  # <class 'list'>

g = ("apple", "banana", "cherry")
print(type(g))  # <class 'tuple'>

h = {"name": "John", "age": 30}
print(type(h))  # <class 'dict'>

i = {"apple", "banana", "cherry"}
print(type(i))  # <class 'set'>

j = frozenset({"apple", "banana", "cherry"})
print(type(j))  # <class 'frozenset'>

k = bytearray(5)
print(type(k))  # <class 'bytearray'>

l = memoryview(bytes(5))
print(type(l))  # <class 'memoryview'>

m = None
print(type(m))  # <class 'NoneType'>