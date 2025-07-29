import numpy as np

print(np.__version__)


arr = np.array([1, 2, 3, 4], ndmin=5)
print(arr)
print(arr.ndim)

print(type(arr))
































print("Hello world")

a=12
b=10

print(a,"+",b,"=",a+b)
print(a,"-",b,"=",a-b)
print(a,"/",b,"=",a/b)
print(a,"*",b,"=",a*b)

num=8
num_sqrt= num**0.5
print(" The square root of %0.2f is %0.2f"%(num, num_sqrt))

num=float(input("Enter any value here"))
if num>0:
    print(" The number is positive")
elif num==0:
    print(" the number is zero")
else:
    print(" The number is negative")

import random
print(random.randint(0,9))
