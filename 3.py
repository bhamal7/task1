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
