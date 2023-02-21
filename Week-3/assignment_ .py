#write a program that solves a quadratic equation 
#Using for loop 
#Draw a diamond 
#draw a triangle 
# Pascals triangle 

import cmath

first_coefficient = int(input("Enter the first coefficient: "))
second_coefficient = int(input("Enter the second coefficient: "))
constant = int(input("Enter the constant: "))

ans1 = -abs(second_coefficient) - cmath.sqrt((second_coefficient**2)-(4*first_coefficient*constant))/(2*first_coefficient)
ans2 = -abs(second_coefficient) + cmath.sqrt((second_coefficient**2)-(4*first_coefficient*constant))/(2*first_coefficient)

print("The answers are "+str(ans1)+" and "+str(ans2))

#using a for loop draw a diamond
M = int(input("Enter the range: "))
for diamond in range(M):
    print("  " * (M - diamond), " *" * (2 * diamond +1))
for diamond in range(M-2,-1,-1):
    print("  " * (M - diamond), " *" * (2 * diamond +1))

print("-----------------------------------------")

#using a for loop draw a triangle
for diamond in range(M):
    print("  " * (M - diamond), " *" * (2 * diamond +1))

print("------------------------------------------")

#using a for loop draw pascals triangle
for l in range(1, M+1):
	for p in range(0, M-l+1):
		print(' ', end='')

	# first element is always 1
	C = 1
	for p in range(1, l+1):

		# first value in a line is always 1
		print(' ', C, sep='', end='')

		#  Binomial Coefficient
		C = C * (l - p) // p
	print()