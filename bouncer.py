age = input("How old are you?\n")

if age:
    age = int(age)
    if age >= 21:
        print("You are good to enter and can drink!")
    elif age >= 18:
        print("you can enter but need a wristband!")
    else:
        print("you can't come ine. little one :(")
else:
    print("please enter an age!")
