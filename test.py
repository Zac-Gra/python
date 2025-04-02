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

print ("{Name}, age {Age}, has chosen {Activity}, meal option: {Meal}. The total cost is   ")
