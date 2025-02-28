# Type Error, Type Checking, Type Conversation


#Type cheacking ------- use python function type()
print(type("hello"))#string
print(type(12345))#integer
print(type(12.345))#float
print(type(True))#boolean


#Type Conversation
user_name = input("Enter your name")
lenght = len(user_name)

print(type("lenght of your name is:"))# string
print(type(lenght)) #integer

print("lenght of your name is:" + str(lenght))