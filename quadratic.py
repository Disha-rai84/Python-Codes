import cmath

a=float(input("enter a value for a"))
b=float(input("enter a value for b"))
c=float(input("enter a value for c"))
d=(b**2)-(4*a*c)
sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)
print(sol1)
print(sol2)