cat_list = []
loop_count = int(1)
while loop_count < 4:
    cat_name = input (f"Enter the name of a cat? ")
    cat_list.append(cat_name) 
    loop_count = loop_count + 1
print( cat_list )