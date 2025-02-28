#Codition
#------------- Nested if / else

print("Welcome to the rollercoaster")
height = int(input("What is your height in cm ?"))
if height > 50:
    print("You can ride thr rollercoaster")
    age= int(input("What is your age ?"))
    if age <= 18:
        print("Please pay 7$.")
    else:
        print("Please pay $12.")    
else:
    print("You can't ride thr rollercoaster")    

#------------if / elif / if
print("Welcome to the rollercoaster")
height = int(input("What is your height in cm ?"))
if height >= 120:
    print("You can ride thr rollercoaster")
    age= int(input("What is your age ?"))
    if age <= 12:
        print("Please pay 5$.")
    elif age <= 18:
        print("Please pay 7$.")
    else:
        print("Please pay $12.")    
else:
    print("You can't ride thr rollercoaster")  