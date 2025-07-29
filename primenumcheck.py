# num = 47
# flag= False

# if num==0 or num==1:
#     print(num,"is not a prime number")
# elif num > 1:
#     for i in range(2,num): 
#         if (num%i==0):
#             flag= True
#             break 

# if flag:
#     print(num, "is not a prime number")
# else:
#     print(num, "is a prime number")



# ---------------------------------------------------------------




num=1
isPrime = True

if num==0 or num==1:
    print(num,"is not a prime number")
else:
    for i in range(2,int(num/2)):
        if(num%i)==0:
            isPrime=False
            break

    if isPrime:
        print("Prime")
    else:
        print("Not Prime")