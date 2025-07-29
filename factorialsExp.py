num =1
f=1
if num<0:
    print("Negative Number ! cannot calculate factorial")
elif num==0 or num==1:
    print(f"The Factorial of given number {num} is 1")
else:
    for i in range(2,num+1):
        f=f*i
    print(f"The Factorial of given number {num} is {f}")