print("Welcome to the camp sign up page please answer these questions truthfully otherwise the bro ryser gonna bash you")

Name = input("What is your name: ")
Age = int(input("What is your age: "))

if Age > 17:
    print("You're not allowed to go")
elif Age < 5:
    print("You're not old enough")
elif Age >= 6 and Age <= 16: 
    print("You're allowed to go")
else:
    print("Invalid age")