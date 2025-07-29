
# num = 7 
# factorial = 1

# if num < 0:
#     print("sorry, factorial don't exist for negative numbers")
# elif num == 0:
#     print(" the factorial for 0 is 1")
# else:
#     for i in range(1,num + 1):
#         factorial = factorial*i
#     print("The factorial of",num ,"is", factorial)  

# 


# num = float(input(" Enter any value in kilometers you need to convert"))
# conv_fac=0.621
# miles= (conv_fac*num)
# print(" %0.1f kilometers is equal to %0.1f miles"%(num,miles))


# celsius=37.5
# # fahrenheit = (celsius*1.8)+32
# # print( "%0.1f celsius is equale to %0.1f fahrenheit" %(celsius, fahrenheit))

# num= float( input("Entet any value"))
# if (num%2==0):
#     print(" The number is even")
# else:
#     print(" The number is an odd number")


num = 4
if num > 1:
    for i in range(2,num):
        if num % i==0:
            print(num,"is not a prime number")
            break
    else:
        print(num,"is a prime number")
else:
    print(num,"is not a prime number")


a= 4
b = 5

print(a,"+",b,"=",a+b)
print(a,"-",b,"=",a-b)
print(a,"*",b,"=",a*b)
print(a,"/",b,"=",a/b)


num = 9
sqrt_fac = num**0.5
print( " The square root of %0.2f is %0.2f"%(num,sqrt_fac))

num1=2
num2=4
num3=12

if (num1>num2) and (num1>num3):
    print(" Number 1 is largest")
elif (num2>num1) and (num2>num3):
    print(" Number 2 is largest")
else:
    print(" Num 3 is the largest")



num =9
factorial = 1
if num<0:
    print( " negative numbers do not have a factorial")
elif num == 0:
    print(" The factorial of 0 is 1")
else:
    for i in range(1,num+1):
        factorial = factorial*i
print(" The factorial of" ,num, "is", factorial)