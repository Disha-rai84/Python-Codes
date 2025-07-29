# # Function Definition - create 
# def addition(a=10,b=10):#parameteres
#     print("a:",a)
#     print("b:",b)
# #    print("Result",a+b)


# # Function Call - use 
# addition(b=15,a=20) #arguments
# addition(40,30)

# #return keyword
# def square(n):
#     print(n*n)
#     return n*n

# # square(10)
# # square(5)

# # print(None*1)

# print("Area of circle : ",3.14*square(4))




# def add(*a):
#     sum=0
#     for i in a:
#         sum+=i
#     return sum


# print((add(10,20)))



# def add(a,b):
#     return a+B


# addition = lambda a,b:a+b

# print(addition(10,22))

b = 20  #global

print(b)

def a():
    global b
    b = 10 #local
    print(b)

a()

print(b)