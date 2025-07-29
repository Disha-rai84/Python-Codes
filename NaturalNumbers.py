num= int(input("enter any number here"))
if num < 0:
    print(" Enter a positive number")
else:
    sum=0
    i=0
    while (i<=num):
        sum +=i
        i+=1
    print(" The sum is",sum)