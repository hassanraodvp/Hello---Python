hungry = True
money = int(input("Enter your amount: "))
restaurant_open = True

if hungry:
    if money == 0:
        print("Just Sleep")
    elif money > 1000:
        if restaurant_open:
            print("Let's have a Party")
        else:
            print("You can't have a Party")
    elif money > 100:
        print("Take Chips & Sprite")
    else:
        print("You can't afford anything")
