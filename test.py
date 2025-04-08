Name = input ("What is your name: ") 
Age = input ("What is your age: ") 

activity_choice = ["1. Music Jam Session", "2. Science Experiments Lab", "3. Sports leadership traning"]
 
print('choose an activity:')
print(f'{activity_choice[0]}')
print(f'{activity_choice[1]}')
print(f'{activity_choice[2]}')
Activity = input ("Enter the number of your chosen activity: ") 

activity_choice = ["1. Standard", "2. Vegetarian", "3. Dairy Free", "4. No Feed"]
 
print('choose an Meal option:')
print(f'{activity_choice[0]}')
print(f'{activity_choice[1]}')
print(f'{activity_choice[2]}')
Meal = input ("Enter the number of your chosen meal: ") 

print (f"{Name}, age {Age}, has chosen activity option {Activity}, meal option: {Meal}. The total cost is 17$. Are you attending?  ")
y_or_no = input ("(Yes/No?): ").lower()
if y_or_no == "yes" : print (f"{Name} is comfirmed for activity option {Activity}, See you there!")
else:
    print (f"{Name} isnt going =( ")
