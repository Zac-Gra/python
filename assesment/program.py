print ("Welcome to the camp sign up page please answer these qustions truthfuly otherwise the bro ryser gonna bash you")
Name = input("What is your name: ")
Age = int(input("What is your age: "))
if Age > 17:
    print("You're not allowed to go (shame) ")
elif Age < 5:
    print("You're not old enough (to bad to sad) ")
elif Age >= 6 and Age <= 16: 
    print("You're allowed to go (yay) ")
else:
    print("not a number goofy ")