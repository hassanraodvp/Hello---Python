# Runtime Errors in Python - Examples

# 1. ZeroDivisionError: Division by zero
def zero_division_error():
    result = 10 / 0  # Cannot divide by zero

# 2. IndexError: List index out of range
def index_error():
    numbers = [1, 2, 3]
    print(numbers[5])  # Only indices 0-2 exist

# 3. KeyError: Dictionary key not found
def key_error():
    person = {"name": "Alice", "age": 25}
    print(person["address"])  # "address" key doesn't exist

# 4. TypeError: Operation on incompatible types
def type_error():
    print("Age: " + 25)  # Can't concatenate string with integer

# 5. NameError: Undefined variable
def name_error():
    print(undefined_var)  # Variable was never defined

# 6. AttributeError: Non-existent attribute
def attribute_error():
    text = "Hello"
    text.append("!")  # Strings don't have append() method

# 7. ValueError: Invalid value conversion
def value_error():
    num = int("abc")  # Can't convert letters to integer

# 8. FileNotFoundError: Missing file
def file_not_found_error():
    with open("nonexistent_file.txt") as f:  # File doesn't exist
        content = f.read()

# 9. ImportError: Module not found
def import_error():
    import non_existent_module  # No such module installed

# 10. KeyboardInterrupt: User interrupted execution
def keyboard_interrupt():
    try:
        while True:
            pass  # Press Ctrl+C to trigger
    except KeyboardInterrupt:
        print("Handled KeyboardInterrupt")

# Uncomment one at a time to see each error in action
if __name__ == "__main__":
    # zero_division_error()
    # index_error()
    # key_error()
    # type_error()
    # name_error()
    # attribute_error()
    # value_error()
    # file_not_found_error()
    # import_error()
    keyboard_interrupt()  # Requires user to press Ctrl+C
    
    print("Note: Uncomment one error function at a time to test")