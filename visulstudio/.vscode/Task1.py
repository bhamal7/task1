# no. 1
variable1 = 11
variable2 = 2.2
variable3 = "string"

# no. 2
variable4 = 2+3j
variable5= 2
print("Before swapping: ")
print("Value of first variable : ", variable4, " and second varible : ", variable5)
#swap it with another variable of type integer
variable4, variable5 = variable5, variable4
print("After swapping: ")
print("Value of first variable : ", variable4, " and second varible : ", variable5)

#no. 3
#with using third variable
variable6 = 22
variable7 = 33
print("Before swapping: ")
print("Value of first variable : ", variable6, " and second varible : ", variable7)
temp = variable6
variable6 = variable7
variable7 = temp
print("After swapping: ")
print("Value of first variable : ", variable6, " and second varible : ", variable7)
#without using third varible
variable8 = 44
variable9 = 55
print("Before swapping: ")
print("Value of first variable : ", variable8, " and second varible : ", variable9)
variable8,variable9 = variable9,variable8
print("After swapping: ")
print("Value of first variable : ", variable8, " and second varible : ", variable9)

# no. 4
input1 = input("Please enter the value: ")
print (input1)
print(input1)1

# no. 5
number1 = int(input("Enter first number between 1- 10: "))
number2 = int(input("Enter second number between 1-10: "))
z = number1 +number2
result = z + 30
print(result)

# no. 6

# no.7
#Upper CamelCase
Bishal = 2
#LOwer CamelCase
bishal = 3
#SnakeCase
bis_hal = 4

#no.8
'''
Yes, variables in Python can be reassigned to a new value that is a different data type from its current value. 
In fact, variables can be reassigned to any valid value in Python, regardless of its current value.

Variables are essentially like an empty box, that can contain something like a string, number, or other value.
 When you assign it a value, the box will contain that value, and when you reassign it, it will empty out the old value, 
 and the new value will be placed inside of it.
 '''