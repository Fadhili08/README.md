#Write a program to print the factorial of a num using functions 

def factorial(n):
    for i in range(0,n):
        fact_n = n * (n-i)
        return fact_n

print(factorial(7))
print(factorial(3))

#Write a program to calculate simple interest
#Simple Interest = P*R*T / 100

def simple_interest(principle,rate,time):
    simple = (principle * rate * time)/100
    print(simple)

simple_interest(50000,3,12)

def linear_Equation(m,x,c):
    y = (m * x) *c
    return 