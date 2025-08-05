
print("My name is Khifsa")
print("My age is 21.")

# print two sentence in one line

print("My name is Khifsa.", "My age is 21.")

# print numbers

print(1, 2, 3, 4, 5)

# print the sum of two numbers

print(23+23)

# print the sum of two numbers

print(23-6)

# print the sum of two numbers

print(2*3)

# print the sum of two numbers

print(2/2)

# USE VARIABLES

print("My Self")

name = "Khifsa"
F_name = "Aurangzeb"
age= 21
B1 = False
B2= True
N= None
F =2.34
print("My name is", name)
print("My father name is", F_name)
print("My age is", age)

# find data type

print(type(name))
print(type(F_name))
print(type(age))
print(type(B1))
print(type(B2))
print(type(N))
print(type(F))

#Find the sum of two numbers by using variables
a = 23
b = 2
sum = a+b
print(sum)
 
#Arithematic operators
a = 10
b = 2
print(a+b)
print(a-b)
print(a*b)
print(a/b) #in division answer is always comes in floating data type
print(a%b) # use to find the reminder
print(a**b) # a^b

#Relational operators (only return true or false "Boolean value")
x= 22
y= 40

print(x==y)# it is use to check that x is equal to y if x is equal y it gives true, if x is not equal to y is give false and the answer is false

print(x!= y)# x is not equal to y, if x is not equal to y its give true, if x is equal to y its give false and the correct answer is true

print(x >= y) #false
print(x > y) #false
print(x < y) #true
print (x <= y)#true

# Assigment operator

sum = 10
sum += sum
print("Sum:" ,sum)
 
sub =10
sub -= 2
print("Sub:",sub)

div = 10
div /= 2
print("Div:", div)

mul = 10
mul **= 2
print("Mul:", mul)

mod = 10
mod %=2
print("Mod:" , mod)
 
# Logical operators (only work on the boolean operators)
# NOT (give the opposite answer, if true its give false, if false its give true)
M = 20
N = 10
print(not(M<N))
print(not False)
print(not True)

#AND (if a value one is false and another one is true its give false,
# in the AND operator both values must be true in this case its give you true)
val1 = 20
val2 = 10
print("And operator:",(val1 > val2) and (val2 < val1)) #true
print ((val1== val2) and (val1 > val2)) # false

# OR (if a single value is true its give true )
print("OR operator:", (val1 == val2) or (val1 > val2)) #true
print((val1< val2) or (val2 >val1)) # false
 
# Type Conversion(it is use to convert the data type)
# Type Coversion
t1 = 2 # data type integer
t2 = 2.5 #data type float

print("Type coversion:",t1 + t2) # it is automatically convert intger data type into float data type it is called "type conversion"
#Float is very superior comparion to the integer in this case that's why python is automatically coverted the data type 

# t3 = "2" ERROR
# t4 = 2.5
# print("Type coversion:",t3 + t4) in this case python give the error because it is not converted string into float because 
# string is superior comparison to the float 

#if you want to convert string data type into float so it is possible to force fully converted this
# in this case you can give A to Z all instructions to the python it is called "Type Casting".

# Type Casting
t3 = float("2") # we use some functions to do a type casting
t4 = 2.5
print("Type casting:",t3 + t4)

#input function (result for input() is always string)

name = input("Enter your name : ")
f_name = input("Enter your Father name : ")
a= input("Enter your age : ")

print("Name : ", name)
print("Father name : ", f_name)
print("Age : ", a)

# ############################# Practice questions ################################
# # Question no 1
# #Write a program to input 2 number and print their sum
A = int(input("Enter first value :")) #int
B = int(input("Enter second value :"))
SUM = A+B
print("Sum of A and B is : ", SUM)

# # Question no 2
# # Write a program to input sides of square and print its area
side = float(input("Enter square side:"))
print("Area of square is = ",side * side )

# Question no 3
# Write a program to input 2 floating point numbers and print their average
c = float(input("Enter first value :")) 
d = float(input("Enter second value :"))
print("Average of two numbers is : ", c*d/2)

# Question no 4
# Write a program to input 2 integer number j and k. print true if j is greater then or equal to k. if not print false
j = int(input(" Enter the value of j :"))
k = int(input(" Enter the value of k :"))
print(j>=k)