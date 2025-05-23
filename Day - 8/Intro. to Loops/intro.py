start = 1 
end = 10

while (start <= end):
    print("Hello!")
    # If we dont use any condition here, it will run infinitely
    # start += 1 (It will print Hello! 10 times)
    # break #(It will print Hello! 1 time)

    num1 = input("Enter a number: ")
    num2 = input("Enter another number: ")

    while (num1 > num2):
        print("Num1 is greater than num2")    
        break

