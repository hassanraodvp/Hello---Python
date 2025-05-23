# Program - 1 
# Program to check num is less than 10 

input_num = float(input("Enter a number: "))

if input_num < 10:
    print("Number is less than 10")
elif input_num == 10:
        print("Number is equal to 10")
else:
    print(f"The Number {input_num} is greater than 10")    

# Program - 2    
# Take input from the user and check it is a Capital letter, Small letter, Digit or Special Character

input_char = input("Enter a single character: ")
if input_char.isupper():
    print("The character is a Capital Letter")
elif input_char.islower():
    print("The character is a Small Letter")
elif input_char.isdigit():
    print("The character is a Digit")
else:
    print("The character is a Special Character")  

# Program - 3
# 

per_num = int(input("Enter a number: "))

if per_num == 100:
    print("Excellent! " + "Grade: A+")
elif per_num > 100:
    print("Invalid Num")    
elif per_num >= 90:
     print("Very Good! " + "Grade: A")
elif per_num >= 80:
     print("Good! " + "Grade: B")
elif per_num >= 70:
     print("Good! " + "Grade: C")
elif per_num >= 60:
     print("Fair! " + "Grade: D")
elif per_num >= 50:
     print("Average! " + "Grade: E")
else:
     print("Try Hard Next Time! (Fail), " + "Grade: F")