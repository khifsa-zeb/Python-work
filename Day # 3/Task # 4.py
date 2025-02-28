#------------Multiple if statement
print("Welcome to the rollercoaster")
height = int(input("What is your height in cm ?"))
bill=0
if height >= 120:
    print("You can ride thr rollercoaster")
    age= int(input("What is your age ?"))
    if age <= 12:
        bill= 5
        print("Child ticket are 5$.")
    elif age <= 18:
        bill= 7
        print("Youth ticket are 7$.")
    else:
        bill= 12
        print("Adult ticket are $12.")    

    wants_photo=input("Do you want to have a photo take? type 'Y' for Yes and 'N' for No ")  
    if wants_photo =="Y":
        bill += 3

    print(f"Your final bill is ${bill}")      
else:
    print("You can't ride thr rollercoaster")  