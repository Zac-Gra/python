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

print ("Chosse an activity to do: \n 1. Cultural immersion. This is for 5 days and is considered “easy” and costs $800.  \n 2. Kayaking and pancakes. This is for 3 days and is considered “moderate” and costs $ 400.  \n 3.Mountain biking. This is for 4 days and is considered “difficult” and costs $900")
Activity = int(input("What would you like to do: "))
if Activity == 1:
    print("Your going to cultural immersion")
elif Activity == 2:
    print("Your going to kayaking and pancakes")
elif Activity == 3:
    print("Your going to mountain biking")
else:
    print("not a number goofy aahh ")