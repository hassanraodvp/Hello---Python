while True:
    age = int(input("Enter your age: "))
    if age < 18:
        print("You are not eligible to vote.")
        continue  # ask again if under 18
    else: 
        print("You can vote!")
        break  # exit loop

for num in range(1 , 10):
    if num % 2 == 0:
        continue
    print(num)