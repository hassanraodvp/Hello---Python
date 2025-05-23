age = int(input("Enter your age: "))
income = int(input("Enter your income: "))
credit_score = int(input("Enter your credit score b/w 0 to 1000: "))

if age >= 18 and income >= 30000:
    if credit_score >= 700:
        print("You are eligible for Premium loan")
    elif  600 <= credit_score < 700:
        print("You are eligible for Standard loan")
    elif credit_score < 600:
        print("High Risk")    
elif income < 30000:
    print("You are not eligible for loan")
else:
    print("Try Improving credit score & income")